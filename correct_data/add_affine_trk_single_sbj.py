#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 22:53:30 2023

@author: chiara
"""
import os
import sys
from pathlib import Path
import nibabel as nib
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)

from config import path_bids_data, tractography_bundle_folder, tractography_bundle_folder_aff
from utils import run_bash_cmd, get_extension
#%%

def add_affine_trk(bids_subj_id="sub-01"):
    fold_trk=f"{path_bids_data}/derivatives/{tractography_bundle_folder}/{bids_subj_id}/"
    fold_trk_aff=f"{path_bids_data}/derivatives/{tractography_bundle_folder_aff}/{bids_subj_id}/"
    paths_trks = [f"{fold_trk}/{trk_file}" for trk_file in os.listdir(fold_trk)]
    path_anat = f"{path_bids_data}/{bids_subj_id}/anat/{bids_subj_id}_T1w.nii.gz"
    
    if not os.path.exists(fold_trk_aff):
        os.makedirs(fold_trk_aff)
        
    for path_trk in paths_trks:
        anat_img=nib.load(path_anat)
        trk = nib.streamlines.load(path_trk)
       
        if not (anat_img.affine == trk.affine).all():
            print("Let's change affine!")
            file_name_ext= os.path.basename(path_trk)
            file_name, ext =os.path.splitext(file_name_ext)[0], os.path.splitext(file_name_ext)[1]
            
            path_tck=f"{fold_trk}/{file_name}.tck"
            path_tck_moved=f"{fold_trk_aff}/{file_name}.tck"

            #path_trk_tmp=f"{fold_trk}/{file_name}_tmp.trk"
            
            bash_commands=[ f"nib-trk2tck {path_trk} -f",
                            f"mv {path_tck} {fold_trk_aff}",
                            f"nib-tck2trk  {path_anat} {path_tck_moved} -f ",
                            f"rm {path_tck_moved}"
                           ]
            
            print()
            print(fold_trk_aff)
            for bash_command in bash_commands:
                run_bash_cmd(bash_command)
            
            

if __name__=="__main__":
    add_affine_trk()