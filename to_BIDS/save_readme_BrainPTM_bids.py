#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:58:12 2023

@author: chiara

Script to save the file readme.md in BrianPTM in BIDS format.
 The md file is taken from 
 ../BrainPTM_to_BIDS/readme_BrainPTM_BIDS.md ---->and copied to----> f"{path_bids_data}/README.md"

The markdown file content is tha
"""

import os
import sys
from pathlib import Path

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)

lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)

from config import path_bids_data
from utils import run_bash_cmd
#%%

path_readme_source = f"{script_dir}/readme_BrainPTM_BIDS.md"
path_readme_bids = f"{path_bids_data}/README.md"

bash_command = f"cp {path_readme_source} {path_readme_bids}"
run_bash_cmd(bash_command)

print(f"Saved to file: {bash_command}")