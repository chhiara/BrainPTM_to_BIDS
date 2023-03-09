#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:16:58 2023

@author: chiara
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
#%%




def cp_regMNI_files(dict_names_correspondance, fold_origin, subj_id_bids, case_id):
    
    fold_to_destination =f"{path_bids_data}/derivatives/register_to_MNI_affine_FA/{subj_id_bids}/"
    if not os.path.exists(fold_to_destination):
        os.makedirs(fold_to_destination)
        
    for file_nm_original, file_nm_new in dict_names_correspondance.items():
        path_to_orig_file = f"{fold_origin}/{file_nm_original}"
        path_to_new_file =  f"{fold_to_destination}/{file_nm_new}"
        
        if os.path.exists(path_to_orig_file):
            bash_command=f"cp {path_to_orig_file} {path_to_new_file}"
            run_bash_cmd(bash_command)
            print(f"{path_to_new_file} saved to file\n")
        else:
            print(f"Alert: {path_to_orig_file} does not exists")
            

def names_regMNI_tracts_train(subj_id_bids="sub-1"):
    tracts=["CST_left", "CST_right", "OR_left", "OR_right"]
    tracts_names_correspondance=dict()
    for t in tracts:
      
        t_new=t.replace("_", "-")

        #add the segmentation file names if the sbj is in group train
        #tracts_names_correspondance[f"{t}_reg_FMRIB58_FA_1mm.nii.gz"] = f"{subj_id_bids}__{t_new}__affined-mni.nii.gz"

        tracts_names_correspondance[f"{t}_reg_FMRIB58_FA_1mm.nii.gz"] = f"{subj_id_bids}_{t_new}_space-MNI152FA_dseg.nii.gz"
    return(tracts_names_correspondance)

def names_regMNI_traintest(subj_id_bids="sub-1"):

    #in this dictionary the keys are the file-names in the original location, while the values are the new file-names in the destion BIDS folder
    
    #-------------files names not eqaul to APSS_Nilab, but more BIDS compliant (even though not completely BIDS compliant)-------------
    dict_names_correspondance= {"brain_mask_reg_FMRIB58_FA_1mm.nii.gz":f"{subj_id_bids}_space-MNI152FA_brain-mask.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gz0GenericAffine.mat": f"{subj_id_bids}_space-MNI152FA_0GenericAffine.mat",
                                "Diffusion_b0_brain_mask_reg_FMRIB58_FA_1mm.nii.gz": f"{subj_id_bids}_space-MNI152FA_brain-mask-b0.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gzInverseWarped.nii.gz": f"{subj_id_bids}_space-individual_FA-MNI.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gzWarped.nii.gz": f"{subj_id_bids}_space-MNI152FA_FA.gz"}

    #-------------files names equal to APSS_Nilab-------------

    # dict_names_correspondance= {"brain_mask_reg_FMRIB58_FA_1mm.nii.gz":f"{subj_id_bids}__brain_mask__affined_binary_mask.nii.gz",
    #                             "FA_reg_FMRIB58_FA_1mm.nii.gz0GenericAffine.mat": f"0GenericAffine.mat",
    #                             "Diffusion_b0_brain_mask_reg_FMRIB58_FA_1mm.nii.gz": f"{subj_id_bids}__brain_mask_b0__affined_binary_mask.nii.gz",
    #                             "FA_reg_FMRIB58_FA_1mm.nii.gzInverseWarped.nii.gz": f"{subj_id_bids}__inv_affined_FA.nii.gz",
    #                             "FA_reg_FMRIB58_FA_1mm.nii.gzWarped.nii.gz": f"{subj_id_bids}__affined_FA.nii.gz.nii.gz"}

    
    
    return dict_names_correspondance

def  cp_reg_files_to_bids_train(case_id="case_1"):
    subj_id_bids = sub_id_to_BIDS(case_id)    
    
    #define name source --> destination
    #it is a dictionary the keys are the file-names in the original location, while the values are the new file-names in the destion BIDS folder

    dict_names_correspondance = names_regMNI_traintest(subj_id_bids)
    tracts_names_correspondance = names_regMNI_tracts_train(subj_id_bids)
    dict_names_correspondance.update(tracts_names_correspondance)
    fold_origin=f"/nilab-qnap/datasets/BrainPTM/train/{case_id}/reg_FA_vs_FMRIB58_FA_1mm/"

    #-----------------------------------------------------------------------------------------
    #cp the files from orgin to destination
    cp_regMNI_files(dict_names_correspondance, fold_origin, subj_id_bids, case_id)
    
            
def  cp_reg_files_to_bids_test(case_id="case_61"):
    
    subj_id_bids = sub_id_to_BIDS(case_id)    
    
    #define name source --> destination
    #in this dictionary the keys are the file-names in the original location, while the values are the new file-names in the destion BIDS folder
    dict_names_correspondance = names_regMNI_traintest(subj_id_bids)
    fold_origin=f"/nilab-qnap/datasets/BrainPTM/test/{case_id}/reg_FA_vs_FMRIB58_FA_1mm/"

    #-----------------------------------------------------------------------------------------
    cp_regMNI_files(dict_names_correspondance, fold_origin, subj_id_bids, case_id)
    



if __name__ =="__main__":
    
    #to run some tests with standard values
    
    cp_reg_files_to_bids_train()
   
    cp_reg_files_to_bids_test()
  