#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 23:57:14 2023

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
from add_affine_trk_single_sbj import add_affine_trk
#%%

tsv_particiapant_path=f"{path_bids_data}/participants.tsv"
df_participants=pd.read_csv(tsv_particiapant_path, sep='\t')

subs_bids_id_train = list(df_participants["participant_id"][df_participants["group"]=="train"].values)

for sub_id in subs_bids_id_train:
    add_affine_trk(sub_id)
    