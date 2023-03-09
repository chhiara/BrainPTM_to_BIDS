#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 18:06:26 2023

@author: chiara
"""

import os
import json
import sys
from pathlib import Path

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)


lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)

from config import path_bids_data
#%%


metadata_t1_path=f"{path_bids_data}/T1w.json"
metadata_dwi_path=f"{path_bids_data}/dwi.json"


dict_metadata_t1={
    "Manufacturer": "GE healthcare, Milwaukee",
    "ManufacturersModelName": "Signa",
    "MagneticFieldStrength":3,
    "ScanningSequence":"T1w",
    "InstitutionName":"Sheba Medical Center at Tel HaShomer, Israel"}



dict_metadata_dwi={
    "Manufacturer": "GE healthcare, Milwaukee",
    "ManufacturersModelName": "Signa",
    "MagneticFieldStrength":3,
    "ScanningSequence":"Diffusion MRI",
    "InstitutionName":"Sheba Medical Center at Tel HaShomer, Israel"}



with open(metadata_t1_path, "w") as outfile:
    json.dump(dict_metadata_t1, outfile)
print(f"saved to file:  {metadata_t1_path}")



with open(metadata_dwi_path, "w") as outfile:
    json.dump(dict_metadata_dwi, outfile)
print(f"saved to file:  {metadata_dwi_path}")
    
    