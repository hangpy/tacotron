#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:09:45 2019

@author: chominjae
"""

from pydub import AudioSegment 
from pydub.silence import split_on_silence 



#AudioSegment.converter = '/Users/chominjae/anaconda3/lib/python3.7/site-packages/ffmpeg'
#AudioSegment.ffprobe   = '/Users/chominjae/anaconda3/lib/python3.7/site-packages/ffprobe'

sound_file = AudioSegment.from_file("/Users/chominjae/Desktop/Capstone/Audio/Audio_original/Casanova/Casanova_5.mp3", format="mp3")
#sound_file = AudioSegment.from_mp3('/Users/chominjae/Desktop/Capstone/Audio/Casanova_1.mp3') 
audio_chunks = split_on_silence(sound_file, 
    # must be silent for at least half a second 
    min_silence_len=400, 

    # consider it silent if quieter than -16 dBFS 
    silence_thresh=-40,keep_silence=100 
) 

for i, chunk in enumerate(audio_chunks): 

    out_file = '/Users/chominjae/Desktop/Capstone/Audio/Audio_split/Casanova_5/Casanova_5_chunk{0}.wav'.format(i) 
    #print("exporting", out_file)
    chunk.export(out_file, format="wav")
    

print("exporting complete")