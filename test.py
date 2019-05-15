
from pydub import AudioSegment
from util.silence import split_on_silence
from glob import glob
from tqdm import tqdm
import os
import argparse
import audioread
import datetime



# out_dir = path.join(path.abspath(''), 'assets', 'Benedict', 'wavs')
# file_pattern = 'BN*_*.wav'
# existing_audio_files = glob(path.join(out_dir, file_pattern))
#
# existing_audio_files.sort(reverse=True)
#
# last_file = path.basename(existing_audio_files[0])
#
#
# print(int(last_file.split('_')[1].split('.')[0]))
#
# print(path.isfile(out_dir))

# def split_operation(args):
# #     # audio file to split
# #     input_file = args.input
# #     target_dir = os.path.join(os.path.abspath(''), 'assets', args.target)
# #     # output directory splitted audio files will be stored
# #     out_dir = os.path.join(os.path.abspath(''), 'assets', args.target, 'wavs')
# #
# #     if not os.path.exists(target_dir):
# #         os.mkdir(target_dir)
# #
# #     if not os.path.exists(out_dir):
# #         os.mkdir(out_dir)
# #
# #     audio_file = AudioSegment.from_file(input_file, format="mp3")
# #
# #     file_pattern = 'BN*_*.wav'
# #     last_index = None
# #     existing_audio_files = glob(os.path.join(out_dir, file_pattern))
# #     if len(existing_audio_files) is not 0:
# #         existing_audio_files.sort(reverse=True)
# #         last_file = os.path.basename(existing_audio_files[0])
# #         last_index = int(last_file.split('_')[1].split('.')[0])
# #     #     becuase the index is started from 0
# #     else:
# #         last_index = 0
# #
# #
# #
# #
# #
# #
# #     audio_file = AudioSegment.from_file(input_file, format="mp3")
# #
# #     # 48khz -> 16khz for google speech api usage
# #     audio_file = audio_file.set_frame_rate(16000)
# #     # multiple channel -> one channel for google speech api usage
# #     audio_file = audio_file.set_channels(1)
# #
# #     print('Split operation is started')
# #
# #     audio_chunks = split_on_silence(audio_file,
# #                                     # must be silent for at least 0.85s
# #                                     min_silence_len=850,
# #
# #                                     # consider it silent if quieter than -16 dBFS
# #                                     silence_thresh=-40, keep_silence=300)
# #     num_of_chunks = len(audio_chunks)
# #
# #     for i, chunk in tqdm(enumerate(audio_chunks, 1), desc='loading...'):
# #         print()
# #
# #     print('Split operation is successfully completed')
# #     print('%d audio chunks were generated' % num_of_chunks)
# #
# # def main():
# #     parser = argparse.ArgumentParser()
# #     parser.add_argument('--input', required=True)
# #     parser.add_argument('--target', required=True)
# #     parser.add_argument('--version', required=True, type=int, help='present version of audio batch file to split')
# #     args = parser.parse_args()
# #
# #     # python split_audio.py --input [path for audio file to split] --target Benedict --version 1
# #     # tacotron/assets/Benedict/wavs directory will be created
# #     split_operation(args)
# #
# #
# # if __name__ == '__main__':
# #     main()


# print(os.stat('/Users/hang/Desktop/dev/voicebrew/assets/Benedict/wavs/BN01_00120.wav').st_size)

dir = os.path.join(os.path.abspath(''), 'assets', 'Benedict', 'wavs')
file_pattern = 'BN*_*.wav'

audio_list = glob(os.path.join(dir, file_pattern))

gross_duration = 0
for file in audio_list:
    gross_duration += audioread.audio_open(file).duration



print(str(datetime.timedelta(seconds=gross_duration)))

