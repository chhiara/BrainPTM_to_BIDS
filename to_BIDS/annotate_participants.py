#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:10:51 2023

@author: chiara

Script to save the file participants.tsv and the corresponding participants.json.
These files collects informations about subjects. In tsv file There is only a descriptive column "group"
that indicate if a subject is in train set (so it was provided of bundles' segmentations) or 
in test (so it was not provided of bundles' segmentations).

"""
#%%
import pandas as pd 
import os
import sys
import json
from pathlib import Path

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)


from config import path_unzipped, path_bids_data, tractography_bundle_folder, bin_mask_bundle_folder
from reorganize_files_to_BIDS_utils import sub_id_to_BIDS
#%%
path_participants_tsv=f"{path_bids_data}/participants.tsv"
path_participants_json=f"{path_bids_data}/participants.json"

subj_folder_dwi_anat_original_train = f"{path_unzipped}/sheba75_data_train/"
case_ids_train_bids = [sub_id_to_BIDS(case_id_original) for case_id_original in os.listdir(subj_folder_dwi_anat_original_train)]

subj_folder_dwi_anat_original_test = f"{path_unzipped}/sheba75_data_test/"
case_ids_test_bids = [sub_id_to_BIDS(case_id_original) for case_id_original in os.listdir(subj_folder_dwi_anat_original_test)]

dict_data={"participant_id":case_ids_train_bids + case_ids_test_bids,
            "group": ["train"]*len(case_ids_train_bids) + ["test"]*len(case_ids_test_bids) }


df_participants=pd.DataFrame(dict_data)

df_participants.to_csv(path_participants_tsv, sep='\t', index=False)
#%%

dict_json={"group": 
        {"LongName": "The group (train, or test) to which each participant belongs.",
        "Description": "Indicate if a subject is in the train set or the test set. The subjects in the train set are intended to train an algorithm to segment the bundles; the subject in the test set are intended to be used only for inference.", 
        "Levels": {"train": "The subject is in the train set, so the bundle's segmentations for that subject are provided to train the algorithm",
                 "test": "The subject is in the test set, so the bundle's segmentations for that subject are NOT provided."
                 }
        }}

with open(path_participants_json, "w") as outfile:
    json.dump(dict_json, outfile)

print(f"saved to file:  {path_participants_json}\n")



