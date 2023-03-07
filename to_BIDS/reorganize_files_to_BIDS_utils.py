#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:05:34 2023

@author: chiara

Collections of functions to reorganize in BIDS BrainPTM's single subject data, 
previously dowloaded from https://brainptm-2021.grand-challenge.org/Dataset/
and unzipped with the script unzip_folders.py

NB: in config.py file are indicated useful variable for the functions:
path_bids_data = path of the BIDS dataset that will be saved
path_unzipped = path of folders downloaded of BrainPTM2021 and unzipped 
 
"""

import os
import sys
from pathlib import Path

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)

from config import path_unzipped,path_bids_data, tractography_bundle_folder, bin_mask_bundle_folder
from utils import sub_id_to_BIDS, run_bash_cmd, get_extension




def save_dwi_BIDS(sub_id, sub_id_bids, subj_folder_original): 
    """
    Save the dwi files of a single case_subject of BrainPRM2021 (Diffusion.nii.gz, Diffusion.bvals, Diffusion.bvecs )
    in BIDS format. The target directory is indicated by the variable path_bids_data defined in config.py  
    """
    #original paths of the BrainPTM files
    path_dwi_original=f"{subj_folder_original}/Diffusion.nii.gz"
    path_bval_original=f"{subj_folder_original}/Diffusion.bvals"
    path_bvec_original=f"{subj_folder_original}/Diffusion.bvecs"
    paths_original_dwi= [path_dwi_original, path_bval_original, path_bvec_original]
    
    #define and create the destination folder to save the files in BIDS
    fold_dwi_bids=f"{path_bids_data}/{sub_id_bids}/dwi/"
    if not os.path.exists(fold_dwi_bids):
        os.makedirs(fold_dwi_bids)
    
    #copy the files in the new destion respecting the BIDS format
    for path_original_dwi in paths_original_dwi:
        file_ext=get_extension(path_original_dwi)
        path_to_bids_dwi=f"{fold_dwi_bids}/{sub_id_bids}_dwi{file_ext}"
        bash_command=f"cp {path_original_dwi}  {path_to_bids_dwi}"
        run_bash_cmd(bash_command)
        
        
def save_anat_BIDS( sub_id, sub_id_bids, subj_folder_original):
    """
    Save the anat files of a single case_subject of BrainPRM2021 (T1.nii.gz, brain_mask.nii.gz)
    in BIDS format. The target directory is indicated by the variable path_bids_data defined in config.py  
    """
    #original paths of the BrainPTM files
    path_t1_original = f"{subj_folder_original}/T1.nii.gz"
    path_brain_mask_original = f"{subj_folder_original}/brain_mask.nii.gz"    
    
    #define and create the destination folder to save the files in BIDS
    fold_anat_bids=f"{path_bids_data}/{sub_id_bids}/anat/"
    if not os.path.exists(fold_anat_bids):
        os.makedirs(fold_anat_bids)

    #copy the files in the new destion respecting the BIDS format
    path_t1_bids= f"{fold_anat_bids}/{sub_id_bids}_T1w" + get_extension(path_t1_original)
    path_brain_mask_bids= f"{fold_anat_bids}/{sub_id_bids}_brain-mask" + get_extension(path_brain_mask_original)

    bash_commands_anat=[f"cp {path_t1_original}  {path_t1_bids}", 
                        f"cp {path_brain_mask_original}  {path_brain_mask_bids}"]
    
    for bash_command in bash_commands_anat:
        run_bash_cmd(bash_command)


def save_tractography_BIDS(sub_id, sub_id_bids, subj_folder_original):
    """
    Save the tractography files of the segmented bundles of a single case_subject of BrainPRM2021 (OR_left.trk, OR_right.trk,
    CST_left.trk, CST_right.trk) in BIDS format. This function is used only for the train subjects that has the ground truth segmentation of the bundles.
    """
    paths_trks_original= [f"{subj_folder_original}/{file}" for file in os.listdir(subj_folder_original)]
    fold_trk_bids=f"{path_bids_data}/derivatives/{tractography_bundle_folder}/{sub_id_bids}/"
    if not os.path.exists(fold_trk_bids):
        os.makedirs(fold_trk_bids)
        
    for path_trk_original in paths_trks_original:
        file_ext=get_extension(path_trk_original)
        file_name_no_ext = (os.path.basename(path_trk_original).replace(file_ext, "")).replace("_", "-")
        path_to_bids_trk=f"{fold_trk_bids}/{sub_id_bids}_{file_name_no_ext}_tract{file_ext}"
        bash_command=f"cp {path_trk_original}  {path_to_bids_trk}"
        run_bash_cmd(bash_command)


def save_dseg_bundles_BIDS(sub_id, sub_id_bids, subj_folder_original):
    """
    Save the binary segmentation files of the segmented bundles of a single case_subject of BrainPRM2021 (OR_left.nii.gz, OR_right.nii.gz,
    CST_left.nii.gz, CST_right.nii.gz) in BIDS format. This function is used only for the train subjects that has the ground truth segmentation of the bundles.
    """
    paths_bundle_original= [f"{subj_folder_original}/{file}" for file in os.listdir(subj_folder_original)]
    fold_bundle_masks_bids=f"{path_bids_data}/derivatives/{bin_mask_bundle_folder}/{sub_id_bids}/"

    if not os.path.exists(fold_bundle_masks_bids):
        os.makedirs(fold_bundle_masks_bids)
        
    for path_mask_original in paths_bundle_original:
        file_ext=get_extension(path_mask_original)
        file_name_no_ext = (os.path.basename(path_mask_original).replace(file_ext, "")).replace("_", "-")
        path_to_bids_bundle_mask=f"{fold_bundle_masks_bids}/{sub_id_bids}_{file_name_no_ext}_dseg{file_ext}"
        bash_command=f"cp {path_mask_original}  {path_to_bids_bundle_mask}"
        
        run_bash_cmd(bash_command)
        
        

def sub_train_BrainPTM_2_BIDS(sub_id = "case_1"):
    """
    Move and rename data of train-subject-data of BrainPTM in BIDS-like format. 
    Takes in input the subject id in BrainPTM format.
    
    """
    print(f"process TRAIN data of  {sub_id}")
    print(f"Data in BIDS saved in  {path_bids_data}\n")
    fold_dwi_anat_original = f"{path_unzipped}/sheba75_data_train/{sub_id}/"   
    fold_trk_original=f"{path_unzipped}/sheba75_streamlines_train/{sub_id}/"
    fold_bundle_mask_original=f"{path_unzipped}/sheba75_tracts_train/{sub_id}/"

    sub_id_bids = sub_id_to_BIDS(sub_id)
    
    #---1. rename and move dwi files---------------------------------

    save_dwi_BIDS(sub_id, sub_id_bids, fold_dwi_anat_original)
    
     #---2. rename and save anat files--------------------------------
    save_anat_BIDS(sub_id, sub_id_bids, fold_dwi_anat_original)
            
    #---3.rename and save tractography files
    save_tractography_BIDS(sub_id, sub_id_bids, fold_trk_original)
    
    #--- 4. rename and save binary masks segmentation of bundles
    save_dseg_bundles_BIDS(sub_id, sub_id_bids, fold_bundle_mask_original)
    

def sub_test_BrainPTM_2_BIDS(sub_id = "case_61"):
    """
    Move and rename data of test-subject-data of BrainPTM in BIDS-like format. 
    Takes in input the subject id in BrainPTM format.
    
    """
    print(f"process TEST data of  {sub_id}")
    print(f"Data in BIDS saved in  {path_bids_data}\n")
    
    subj_folder_dwi_anat_original = f"{path_unzipped}/sheba75_data_test/{sub_id}/"   
    sub_id_bids = sub_id_to_BIDS(sub_id)
    
    #---1. rename and move dwi files---------------------------------
    save_dwi_BIDS(sub_id, sub_id_bids, subj_folder_dwi_anat_original)
    
     #---2. rename and save anat files--------------------------------
    save_anat_BIDS(sub_id, sub_id_bids, subj_folder_dwi_anat_original)
            
   

    

    
    

if __name__ =="__main__":
    
     #to run some tests with default values of sub_id
     
    sub_train_BrainPTM_2_BIDS()
    sub_test_BrainPTM_2_BIDS()
    