#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:13:23 2023

@author: chiara

Correct bvals Brainptm2021 and save them in derivative/bval_bvec_corrected/
"""

import os
import sys
from pathlib import Path
import nibabel as nib
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)

from config import path_bids_data, bvec_bval_corrected_folder
from utils import run_bash_cmd, get_extension
#%%


def correct_bvec(fold_out,bids_subj_id):
    path_bvec_corrected=f"{fold_out}/{bids_subj_id}_flip-x_dwi.bvec"
    
    
    path_bvec = f"{path_bids_data}/{bids_subj_id}/dwi/{bids_subj_id}_dwi.bvec"
    
    #NB code to treat cases where there are more lines in bvals... even though
    #there is only one line  
    
    with open(path_bvec, "r") as f:
        lines = f.readlines()
    
    new_lines=[]
    for i,line in enumerate(lines):
        if i==0:
            new_line=" ".join([str(float(x)*-1) if x!="0" else x for x in line.split(" ")]) +"\n"
        else:
            new_line=line
        
        #print(new_line)
        #print()
        new_lines.append(new_line)
    
    with open(path_bvec_corrected, "w") as f:
        f.writelines(new_lines)
    

def correct_bval(fold_out, bids_subj_id):
    
    path_bval_corrected=f"{fold_out}/{bids_subj_id}_mult-1000_dwi.bval"
    
    
    path_bval = f"{path_bids_data}/{bids_subj_id}/dwi/{bids_subj_id}_dwi.bval"
    
    #NB code to treat cases where there are more lines in bvals... even though
    #there is only one line  
    
    with open(path_bval, "r") as f:
        lines = f.readlines()
    
    new_lines=[]
    for line in lines:
        new_line=" ".join([str( round( (float(x)*1000),4 )) for x in line.split(" ")]) +"\n"
        print(new_line)
        print()
        new_lines.append(new_line)
    
    with open(path_bval_corrected, "w") as f:
        f.writelines(new_lines)
    
  
            
            
def correct_bval_bvec(bids_subj_id="sub-01"):
    
    fold_out=f"{path_bids_data}/derivatives/{bvec_bval_corrected_folder}/{bids_subj_id}/"
    
    if not os.path.exists(fold_out):
        os.makedirs(fold_out)
    
    correct_bval(fold_out, bids_subj_id)
    
    correct_bvec(fold_out, bids_subj_id)
    
    
    
if __name__=="__main__":
    correct_bval_bvec()