#!/bin/bash

cd to_BIDS
#1. unzip dowloaded folders
python unzip_folders.py

#2. reoriganize and rename train subjects unzipped data
python train_subjs_to_BIDS.py

#3.  reoriganize and rename test subjectsunzipped  data
python test_subjs_to_BIDS.py

#4. create participants.tsv and participants.json that indicate if a subject is the group train or test
python annotate_participants.py

#5. copy the readme provided by this git repository at ../BrainPTM_to_BIDS/readme_BrainPTM_BIDS.md --> to--> the BIDS dataset f"{path_bids_data}/README.md 
python save_readme_BrainPTM_bids.py

#6.save json files decribing the dataset at:
#-  parent directory f"{path_bids_data}/ to describe row data
#-  directories of derivatives tractograhy and binary masks to describe each derivative data
python write_save_description_dataset.py

 

