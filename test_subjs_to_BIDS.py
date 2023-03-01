#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:00:57 2023

@author: chiara

Script to rename and move files referred to TEST data of the dataset BrainPTM.

The train data have:
    - dwi data
    - anat data 
  
        
For the test data the segmentation of the bundles are not provided, differently from the train data.

The data were dowloaded from https://brainptm-2021.grand-challenge.org/Dataset/
and unzipped with the script unzip_folders.py

"""


import os
import sys
from pathlib import Path
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

from config import path_bids_data, path_unzipped
from reorganize_files_to_BIDS_utils import sub_test_BrainPTM_2_BIDS
#%%

subj_folder_dwi_anat_original = f"{path_unzipped}/sheba75_data_test/"

case_ids_original = [case_id_original for case_id_original in os.listdir(subj_folder_dwi_anat_original)]
#%%
for case_id in case_ids_original:
    sub_test_BrainPTM_2_BIDS(case_id)


