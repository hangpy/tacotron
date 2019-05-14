#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:09:45 2019

@author: chominjae
"""

from pydub import AudioSegment
# from pydub.silence import split_on_silence
from util.silence import split_on_silence
import os
import argparse



def split_operation(args):

    # audio file to split
    input_file = args.input
    target_dir = os.path.join(os.path.abspath(''), 'assets', args.target)
    # output directory splitted audio files will be stored
    out_dir = os.path.join(os.path.abspath(''), 'assets', args.target, 'wavs')

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)


    audio_file = AudioSegment.from_file(input_file, format="mp3")

    # 48khz -> 16khz for google speech api usage
    audio_file = audio_file.set_frame_rate(16000)
    # multiple channel -> one channel for google speech api usage
    audio_file = audio_file.set_channels(1)

    print('Split operation is started')

    audio_chunks = split_on_silence(audio_file,
                                    # must be silent for at least half a second
                                    min_silence_len=400,

                                    # consider it silent if quieter than -16 dBFS
                                    silence_thresh=-40, keep_silence=100
                                    )



    for i, chunk in enumerate(audio_chunks):
        out_file = os.path.join(out_dir, 'BN%02d_%05d.wav' % (args.version, i))
        chunk.export(out_file, format="wav")

    print('Split operation is completed')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--target', required=True)
    parser.add_argument('--version', required=True, type=int, help='present version of audio batch file to split')
    args = parser.parse_args()

    # python split_audio.py --input [path for audio file to split] --target Benedict --version 1
    # tacotron/assets/Benedict/wavs directory will be created
    split_operation(args)


if __name__ == '__main__':
    main()