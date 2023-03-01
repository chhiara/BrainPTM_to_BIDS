#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:09:36 2023

@author: chiara
"""
#path to zipped dowloaded data
path_zipped="/home/chiara/datasets/BrainPTM2021/zip/"

#path to unzipped data
path_unzipped="/home/chiara/datasets/BrainPTM2021/unzip/"

#path to the dataset created and converted in BIDS format
path_bids_data = "/home/chiara/datasets/BrainPTM_BIDS/"


#folders names of the derivatives folders containing:
#- the trk files referred to each tract
tractography_bundle_folder="tractography"

#- the binary files referred to each tract
bin_mask_bundle_folder="binary_masks"
