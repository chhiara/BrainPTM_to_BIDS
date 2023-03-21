#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:58:28 2023

@author: chiara


Save json files decribing the dataset:
  
    - f"{path_bids_data}/derivatives/{correct_bval_bvec}/dataset_description.json"   
        decribe the derivative data: bvals -> multiplied by 1000 
                                     bvecs  -> flipped X direction 
    - f"{path_bids_data}/derivatives/{tractography_bundle_folder_aff}/dataset_description.json"   
          decribe the derivative data: trk files -> with correct affine 
          
  
"""

import os
import sys
import json
from pathlib import Path

script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)


lib_parent_dir = str(Path(script_dir).parent.absolute()) + "/"
sys.path.append(lib_parent_dir)

from config import path_unzipped,path_bids_data, bvec_bval_corrected_folder,tractography_bundle_folder_aff
#%%
path_data_description_correct_bval_bvecs=f"{path_bids_data}/derivatives/{bvec_bval_corrected_folder}/dataset_description.json"
path_data_description_trk_affine=f"{path_bids_data}/derivatives/{tractography_bundle_folder_aff}/dataset_description.json"


#----------------------------------------------------------------------
#----description json of the derivative bval bvecs data ---------------------------------
#----------------------------------------------------------------------
dict_data_bvalbvecs={"Name": "bvals and bvecs corrected",
                      "BIDSVersion":"1.8.0",
                      "DatasetType": "derivative",
                      "ReferencesAndLinks": ["https://brainptm-2021.grand-challenge.org/", "https://doi.org/10.1109/TMI.2019.2954477", "https://doi.org/10.1109/ISBI45749.2020.9098454"],
                      "Authors": [
                        "Chiara Riccardi" 
                        
                      ],
                      "Acknowledgements": "Sheba Medical Center at Tel HaShomer, Israel. CIlab, The Computational Imaging lab",
                      "HowToAcknowledge":"Please cite the papers:  https://doi.org/10.1109/TMI.2019.2954477 and https://doi.org/10.1109/ISBI45749.2020.9098454.",
                      "SourceDatasets": [{ "link" : "https://brainptm-2021.grand-challenge.org/"}],
                      "GeneratedBy": {
                                                          "Name": "Python",
                                                          "Version": "3.9.12", 
                                                          "Description": "The original bvals were multiplied by 1000 and saved to file; the original bvecs were flipped along the x axis and saved to file" ,
                                                           "CodeURL":"https://github.com/chhiara/BrainPTM_to_BIDS.git" }
                      
                    }

with open(path_data_description_correct_bval_bvecs, "w") as outfile:
    json.dump(dict_data_bvalbvecs, outfile)
    
print(f"saved to file:  {path_data_description_correct_bval_bvecs}")


#----------------------------------------------------------------------
#----description json of the derivative tractography with affine-------
#----------------------------------------------------------------------
dict_tract_affine={"Name": "bvals and bvecs corrected",
                      "BIDSVersion":"1.8.0",
                      "DatasetType": "derivative",
                      "ReferencesAndLinks": ["https://brainptm-2021.grand-challenge.org/", "https://doi.org/10.1109/TMI.2019.2954477", "https://doi.org/10.1109/ISBI45749.2020.9098454"],
                      "Authors": [
                        "Chiara Riccardi" 
                        
                      ],
                      "Acknowledgements": "Sheba Medical Center at Tel HaShomer, Israel. CIlab, The Computational Imaging lab",
                      "HowToAcknowledge":"Please cite the papers:  https://doi.org/10.1109/TMI.2019.2954477 and https://doi.org/10.1109/ISBI45749.2020.9098454.",
                      "SourceDatasets": [{ "link" : "https://brainptm-2021.grand-challenge.org/"}],
                      "GeneratedBy": {
                                                          "Name": "Python",
                                                          "Version": "3.9.12", 
                                                          "Description": "The original trk files had no the correct affine. The affine of the T1w was added to trk files by using nibabel commands" ,
                                                           "CodeURL":"https://github.com/chhiara/BrainPTM_to_BIDS.git" }
                      
                    }

with open(path_data_description_trk_affine, "w") as outfile:
    json.dump(dict_tract_affine, outfile)
    
print(f"saved to file:  {path_data_description_trk_affine}")



    

    
    
 