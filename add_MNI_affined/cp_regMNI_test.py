#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:04:40 2023

@author: chiara

Retrieve MNI registered data for test cases and copy to BIDS dataset-
"""


import os
import sys
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)
from config import path_bids_data,path_unzipped 
from reorganize_files_to_BIDS_utils import sub_id_to_BIDS, run_bash_cmd
from cp_regMNI_files import cp_reg_files_to_bids_test

    
#---- retrieve MNI registered data for test cases and copy to BIDS dataset------------

subj_folder_dwi_anat_original_test = f"{path_unzipped}/sheba75_data_test/"
case_ids_original_test = [case_id_original for case_id_original in os.listdir(subj_folder_dwi_anat_original_test)]

for id_test in case_ids_original_test:
    cp_reg_files_to_bids_test(case_id=id_test)
    
