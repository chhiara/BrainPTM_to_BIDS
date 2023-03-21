#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 16:58:28 2023

@author: chiara


Save json files decribing the dataset:
  
    - f"{path_bids_data}//BrainPTM_BIDS/derivatives/register_to_MNI_affine_FA/dataset_description.json"   
       These data were registered with ants software with an affine transformation. The reference for the registration was the FA in MNI space provided from FSL:
       and described in https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FMRIB58_FA 

  
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
path_data_description_mni_fa=f"{path_bids_data}/derivatives/register_to_MNI_affine_FA/dataset_description.json"


#----------------------------------------------------------------------
#----description json of the derivative bval bvecs data ---------------------------------
#----------------------------------------------------------------------
dict_data_mnifa={"Name": "bvals and bvecs corrected",
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
                                                          "Name": "ants",
                                                          "Version": "2.3.1", 
                                                          "Description": "From the dwi of each subject the FA was computed with mrtrix. Then the FA was registered using as fixed image the FA template in MNI space provided by FSL and described at https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FMRIB58_FA " ,
                                                           "CodeURL":"https://github.com/chhiara/BrainPTM_to_BIDS.git" }
                                                       
                    }

with open(path_data_description_mni_fa, "w") as outfile:
    json.dump(dict_data_mnifa, outfile)
    
print(f"saved to file:  {path_data_description_mni_fa}")



#todo: save space files relative to each individual

#"SpatialReference": {"space-MNI152FA":"FA template in MNI space provided by FSL and described at https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/FMRIB58_FA",
                                                                                #"space-individual": "uri to FA file to add"} }  #tododoooo
                      

