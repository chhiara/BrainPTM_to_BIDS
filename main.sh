#!/bin/bash

#1. unzip dowloaded folders
python unzip_folders.py

#2. reoriganize and rename train subjects unzipped data
python train_subjs_to_BIDS.py

#3.  reoriganize and rename test subjectsunzipped  data
python train_subjs_to_BIDS.py

#4. create json files to describe the dataset




