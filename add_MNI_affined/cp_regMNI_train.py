#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:02:41 2023

@author: chiara

Retrieve MNI registered data for train cases and copy to BIDS dataset-

"""

import os
import sys
from pathlib import Path

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)

from config import path_bids_data,path_unzipped 
from utils import sub_id_to_BIDS, run_bash_cmd
from cp_regMNI_utils import cp_reg_files_to_bids_train

    
#----2 retrieve MNI registered data for train cases and copy to BIDS dataset------------

subj_folder_dwi_anat_original_train = f"{path_unzipped}/sheba75_data_train/"
case_ids_original_train = [case_id_original for case_id_original in os.listdir(subj_folder_dwi_anat_original_train)]

for id_train in case_ids_original_train:
    cp_reg_files_to_bids_train(case_id=id_train)
    
