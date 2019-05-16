#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 00:40:58 2019

@author: chominjae
"""

'''
depreciation
'''

# import os
# from glob import glob
# import pandas as pd
# import argparse
#
# def generate_metadata(args):
#     f_filter = ["mp3", "wav"] # a list containing the desired file extensions to be matched
#     m = [] # final match list
#     in_dir = args.input
#     # out_dir = os.path.join(os.path.abspath(''), args.output, args.target)
#
#     for f_path in glob(os.path.join(in_dir, '**'), recursive=True): # loop directory recursively
#         f_name = os.path.basename(f_path) # get the filename
#         f_ext = f_name.split(".")[-1].lower() # get the file extension and lower it for comparison.
#
#         if f_ext in f_filter: # filter files by f_filter
#
#             label = f_name+"|"
#             #label = f_name[0] + f_ext[-1] # as per your example, first char of file_name and last of file_ext
#             #m.append([f_path, f_name, f_ext, label]) # append to match list
#             m.append(label)
#             #print(f_path, f_name, f_name, label)
#
#     #df = pd.DataFrame(m, columns=['f_path', 'f_name', 'f_ext', 'label']) # create a dataframe from match list
#     df = pd.DataFrame(m, columns=['label']) # create a dataframe from match list
#     df.to_csv(os.path.join(in_dir, 'metadata.csv'), index=False, header=False) # create csv from df
#
#
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--input', required=True)
#     args = parser.parse_args()
#     generate_metadata(args)
#
#
#
# if __name__ == '__main__':
#   main()