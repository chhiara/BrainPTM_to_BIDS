#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 1 12:50:41 2023

@author: chiara
Script that unzip the folders of the datset BrainPTM2021 ,
downloaded from https://brainptm-2021.grand-challenge.org/Dataset/

"""
import os
import sys
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)
from config import path_zipped, path_unzipped
#%%

datafolders=[f"{path_zipped}/{fold}" for fold in os.listdir(path_zipped)]
datafolders_unzipped = [path_unzipped + fold.replace(".zip", "") for fold in os.listdir(path_zipped)]

#%%
for i,data_fold in enumerate(datafolders):
    destination_folder = datafolders_unzipped[i]
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    print(f"unzip {data_fold} and save unzipped folder to {destination_folder}")
    
    bash_command=f"unzip -d {destination_folder} {data_fold}"
    print(bash_command)
    print()
    os.system(bash_command)


