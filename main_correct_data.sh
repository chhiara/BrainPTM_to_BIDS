#!/bin/bash

#Created on Fri Mar 17 18:33:03 2023

#@author: chiara

cd correct_data
#1. add affine to trk files and save them in derivative
python add_affine_trk_train_sbjs.py

#2. correct bvals and bvecs: bvals are multiplied by 1000, while the bvecs are X flipped
python correct_bval_bvec_sbjs.py 

#3.add description of the derivative datasets
python save_descriptions_json.py
