#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 15:48:51 2023

@author: chiara
"""


import os
import sys
from pathlib import Path
import pandas as pd

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)


lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)


from config import path_bids_data
from correct_bval_bvec_single_sbj import correct_bval_bvec
#%%

tsv_particiapant_path=f"{path_bids_data}/participants.tsv"
df_participants=pd.read_csv(tsv_particiapant_path, sep='\t')

subs_bids_ids = list(df_participants["participant_id"].values)
#%%
for sub_id in subs_bids_ids:
    correct_bval_bvec(sub_id)
    