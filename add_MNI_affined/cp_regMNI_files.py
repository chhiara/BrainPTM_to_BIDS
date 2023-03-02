#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:10:35 2023

@author: chiara

Script to copy in BIDS folder the files registered with affine in MNI to BIDS folder destination.
Those files were previously computed and were saved at : 
    /nilab-qnap/datasets/BrainPTM/<group>/<case_id>/reg_FA_vs_FMRIB58_FA_1mm/
    
    where <group> is either "train" or "test"
          <case-id> is the case-id in BrainPTM format

TODO: clarify if it a problem for successive analysis have names more BIDS compliant and not analogous to APSS_Bundles_Nilab
    
"""
import os
import sys
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)
from config import path_bids_data,path_unzipped 
from reorganize_files_to_BIDS_utils import sub_id_to_BIDS, run_bash_cmd


def  cp_reg_files_to_bids(case_id="case_1", group_train=True):
    g="train" if group_train else "test"
    subj_id_bids = sub_id_to_BIDS(case_id)
    tracts=["CST_left", "CST_right", "OR_left", "OR_right"]
    dir_reg_MNI_sbj=f"/nilab-qnap/datasets/BrainPTM/{g}/{case_id}/reg_FA_vs_FMRIB58_FA_1mm/"
    fold_to_destination =f"{path_bids_data}/derivatives/register_to_MNI_affine/"

    if not os.path.exists(fold_to_destination):
        os.makedirs(fold_to_destination)
        
    #in this dictionary the keys are the file-names in the original location, while the values are the new file-names in the destion BIDS folder
    
   
    """
    #--------------- files names with the files analogue to APSS_Nilab ------------------
    dict_names_correspondance= {"brain_mask_reg_FMRIB58_FA_1mm.nii.gz":f"{subj_id_bids}__affined_brain_mask.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gz0GenericAffine.mat": "0GenericAffine.mat",
                                "Diffusion_b0_brain_mask_reg_FMRIB58_FA_1mm.nii.gz": f"{subj_id_bids}__affined_brain_maskb0.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gzInverseWarped.nii.gz": f"{subj_id_bids}__inverse_affined_FA.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gzWarped.nii.gz": f"{subj_id_bids}__affined_FA.nii.gz"}
    
    if group_train:
        for t in tracts:
            #add the segmentation file names if the sbj is in group train
            dict_names_correspondance[f"{t}_reg_FMRIB58_FA_1mm.nii.gz"] = f"{subj_id_bids}_{t}__affined_binary_masks.nii.gz"
    #----------------------------------------------------------------------------------      
    """
    
    
    #-------------files names not eqaul to APSS_Nilab, but more BIDS compliant ---------------
    dict_names_correspondance= {"brain_mask_reg_FMRIB58_FA_1mm.nii.gz":f"{subj_id_bids}_brain-mask_affined-mni.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gz0GenericAffine.mat": f"{subj_id_bids}_0GenericAffine_affined-mni.mat",
                                "Diffusion_b0_brain_mask_reg_FMRIB58_FA_1mm.nii.gz": f"{subj_id_bids}_brain-mask-b0_affined-mni.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gzInverseWarped.nii.gz": f"{subj_id_bids}_FA_inv-affined-mni.nii.gz",
                                "FA_reg_FMRIB58_FA_1mm.nii.gzWarped.nii.gz": f"{subj_id_bids}_FA_affined-mni.nii.gz"}
    
    if group_train:
        for t in tracts:
            t_new=t.replace("_", "-")
            #add the segmentation file names if the sbj is in group train
            dict_names_correspondance[f"{t}_reg_FMRIB58_FA_1mm.nii.gz"] = f"{subj_id_bids}_{t_new}_affined-mni.nii.gz"
          
    #-----------------------------------------------------------------------------------------
    
    
    for file_nm_original, file_nm_new in dict_names_correspondance.items():
        path_to_orig_file = f"{dir_reg_MNI_sbj}/{file_nm_original}"
        path_to_new_file =  f"{path_bids_data}/derivatives/register_to_MNI_affine/{file_nm_new}"
        
        if os.path.exists(path_to_orig_file):
            bash_command=f"cp {path_to_orig_file} {path_to_new_file}"
            run_bash_cmd(bash_command)
            print(f"{path_to_new_file} saved to file\n")
        else:
            print(f"Alert: {path_to_orig_file} does not exists")





if __name__ =="__main__":
    
    #cp_reg_files_to_bids()
    
    #----1 retrieve MNI registered data for test cases and copy to BIDS dataset------------
    #retrieve case-id if GROUP=test
    
    subj_folder_dwi_anat_original_test = f"{path_unzipped}/sheba75_data_test/"
    case_ids_original_test = [case_id_original for case_id_original in os.listdir(subj_folder_dwi_anat_original_test)]
    for id_test in case_ids_original_test:
        cp_reg_files_to_bids(case_id=id_test, group_train=False)
        
        
    #----2 retrieve MNI registered data for train cases and copy to BIDS dataset------------
    
    subj_folder_dwi_anat_original_train = f"{path_unzipped}/sheba75_data_train/"
    case_ids_original_train = [case_id_original for case_id_original in os.listdir(subj_folder_dwi_anat_original_train)]
    for id_test in case_ids_original_train:
        cp_reg_files_to_bids(case_id=id_test, group_train=False)
        
