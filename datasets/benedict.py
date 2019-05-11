# 멀티프로세싱을 위한 모듈
# 멀티 쓰레딩, 멀티프로세싱을 위한 클래스들이 있다.
from concurrent.futures import ProcessPoolExecutor
# 하나 이상의 인수가 이미 채워진 함수의 새 버전을 만들기 위해 사용
# 함수의 새 버전은 그 자체를 기
from functools import partial
# 다차원 배열을 처리하는데 필요한 여러 유용한 기능 제
import numpy as np
# os에서 제공하는 기능을 담음 모듈
import os
# 유틸 디렉토리에서 audio 파일 가져오기
from util import audio


def build_from_path(in_dir, out_dir, num_workers=1, tqdm=lambda x: x):
  '''Preprocesses the LJ Speech dataset from a given input path into a given output directory.

    Args:
      in_dir: The directory where you have downloaded the LJ Speech dataset
      out_dir: The directory to write the output into
      num_workers: Optional number of worker processes to parallelize across
      tqdm: You can optionally pass tqdm to get a nice progress bar

    Returns:
      A list of tuples describing the training examples. This should be written to train.txt
  '''

  # We use ProcessPoolExecutor to parallelize across processes. This is just an optimization and you
  # can omit it and just call _process_utterance on each input if you want.

  executor = ProcessPoolExecutor(max_workers=num_workers)
  futures = []
  index = 1
  with open(os.path.join(in_dir, 'metadata.csv'), encoding='utf-8') as f:
    # csv파일을 돌면서 각 파일마다 멜스펙토그램 학습파일 생성.
    for line in f:
      parts = line.strip().split('|')
      wav_path = os.path.join(in_dir, 'wavs', '%s.wav' % parts[0])
      text = parts[2]
      # process_utterance 로직 실행
      # submit(fn, *arg, **kwargs) 함수 fn에 대해 주어진 인자들을 전달하여 실행할 수 있는
      # executor는 Future 객체를 리턴. 해당 함수는 호출 즉시 스케줄링됨.
      # Future 클래스는 콜러블 객체의 비동기 실행을 캡슐화합니다.
      # Future 인스턴스는 Executor.submit() 에 의해 생성됩니다.
      futures.append(executor.submit(partial(_process_utterance, out_dir, index, wav_path, text)))
      index += 1
  return [future.result() for future in tqdm(futures)]

# utterance: 발성
def _process_utterance(out_dir, index, wav_path, text):
  '''Preprocesses a single utterance audio/text pair.

  This writes the mel and linear scale spectrograms to disk and returns a tuple to write
  to the train.txt file.

  Args:

    스펙토그렘 정보 저장할 디렉토리 명시
    out_dir: The directory to write the spectrograms into

    순서 명시
    index: The numeric index to use in the spectrogram filenames.

    오디오 파일 포함한 포함한 디렉토리 명시
    wav_path: Path to the audio file containing the speech input

    오디오 파일에 대한 텍스트 파일 명시한 경로
    text: The text spoken in the input audio file

  Returns:
    A (spectrogram_filename, mel_filename, n_frames, text) tuple to write to train.txt
  '''

  # Load the audio to a numpy array:
  wav = audio.load_wav(wav_path)

  # Compute the linear-scale spectrogram from the wav:
  spectrogram = audio.spectrogram(wav).astype(np.float32)
  n_frames = spectrogram.shape[1]

  # Compute a mel-scale spectrogram from the wav:
  mel_spectrogram = audio.melspectrogram(wav).astype(np.float32)

  # Write the spectrograms to disk:
  spectrogram_filename = 'benedict-spec-%05d.npy' % index
  mel_filename = 'benedict-mel-%05d.npy' % index
  np.save(os.path.join(out_dir, spectrogram_filename), spectrogram.T, allow_pickle=False)
  np.save(os.path.join(out_dir, mel_filename), mel_spectrogram.T, allow_pickle=False)

  # Return a tuple describing this training example:
  return (spectrogram_filename, mel_filename, n_frames, text)