#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:34:18 2023

@author: chiara
"""

import os
import sys
from pathlib import Path

def get_extension(path_file):
    """
    Return file extension of a file, even when there are multiple suffixes. Eg: with img.nii.gz, returns ".nii.gz"
    """
    file_ext="".join(Path(path_file).suffixes)
    return file_ext

def run_bash_cmd(bash_command):
    """
    Run bash command with os.sytem and print it
    """
    print(bash_command, "\n")
    os.system(bash_command)
    
def sub_id_to_BIDS(sub_id):
    """
    Convert the case_id from BrainPTM2021 format to BIDS format
    eg: taking in input "case_1"  ---> returns --> sub-1
    """
    sub_id_bids = "sub-"+sub_id.split("_")[1]
    return sub_id_bids

