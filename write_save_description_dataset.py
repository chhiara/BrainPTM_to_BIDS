#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 13:09:07 2023

@author: chiara

Save json files decribing the dataset:
    - {path_bids_data}/dataset_description.json  
        describe the row data
    - f"{path_bids_data}/derivatives/{tractography_bundle_folder}/dataset_description.json"   
        decribe the derivative data: tractography, thata are the tractography segmentation bundles
        
    - f"{path_bids_data}/derivatives/{bin_mask_bundle_folder}/dataset_description.json"
    decribe the derivative data: binary_masks, thata are the binary masks of the segmented bundles, derived from the tractography data
"""

import os
import sys
import json
script_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_dir)
from config import path_unzipped,path_bids_data, tractography_bundle_folder, bin_mask_bundle_folder
#%%
path_data_description_json=f"{path_bids_data}/dataset_description.json"
path_data_description_tractogr_json=f"{path_bids_data}/derivatives/{tractography_bundle_folder}/dataset_description.json"
path_data_description_bin_masks_json=f"{path_bids_data}/derivatives/{bin_mask_bundle_folder}/dataset_description.json"

#----------------------------------------------------------------------
#----description json of the row data ---------------------------------
#----------------------------------------------------------------------
dict_data_row={"Name": "BrainPTM2021",
                      "BIDSVersion":"1.8.0",
                      "DatasetType": "raw",
                      "ReferencesAndLinks": ["https://brainptm-2021.grand-challenge.org/", "https://doi.org/10.1109/TMI.2019.2954477", "https://doi.org/10.1109/ISBI45749.2020.9098454"],
                      "Authors": [
                        "Ilya Nelkenbaum",
                        "Noa Barzilay",
                        "Arnaldo Mayer"
                      ],
                      "Acknowledgements": ["Sheba Medical Center at Tel HaShomer, Israel. CIlab, The Computational Imaging lab"],
                      "HowToAcknowledge":"Please cite the papers:  https://doi.org/10.1109/TMI.2019.2954477 and https://doi.org/10.1109/ISBI45749.2020.9098454.",
                      "SourceDatasets": "https://brainptm-2021.grand-challenge.org/"
                    }

with open(path_data_description_json, "w") as outfile:
    json.dump(dict_data_row, outfile)
    
    
    
#------------------------------------------------------------------------------
#----descriptive json of the derivative data of the bundle segmentation's tractography
#-------------------------------------------------------------------------------


dict_data_tractog = dict_data_row #base information shared among jsons files

dict_data_tractog["DatasetType"] = "derivative"
dict_data_tractog["Name"] = "tractography bundle-segmentations"
dict_data_tractog["GeneratedBy"]=[ {
                                    "Name": "MrDiffusion",
                                    "Version": "",  #!missing!
                                    "Description": "From dwi data, tensor fitting and DEC (directionally encoded color) maps were computed with MrDiffusion."
                                      },
                                    
                                    {"Name": "Manual",
                                    "Description": "ROIs to indentify Corticospinal tract and optic radiation were manually segmented by experts in T1w and DEC images. In particular, for the Optic radiation lateral geniculate nucleus (LGN) of the thalamus and the calcarine sulcus in the occipital lobe were segmented. For the corticospinal tract precentral-gyrus (posterior frontal lobe) and the brain stem were segmented"
                                    },
                                    
                                    {
                                      "Name": "ConTrack",
                                      "Version": "",   #!missing!
                                      "Description": "Probabilistic tractography seeded at specific cortex ROIs, manually segmented. For Optic radiations the ROIs were the lateral geniculate nucleus (LGN) of the thalamus and the calcarine sulcus in the occipital lobe. For the CST the ROIs were precentral-gyrus (posterior frontal lobe) and the brain stem."
                                        }
                                  
                                            ]


with open(path_data_description_tractogr_json, "w") as outfile:
    json.dump(dict_data_tractog, outfile)
    
    
#------------------------------------------------------------------------------------
#----descriptive json of the derivative data of the bundle segmentation's binary masks
#-------------------------------------------------------------------------------------
dict_data_bin_bundles = dict_data_tractog

dict_data_bin_bundles["DatasetType"] = "derivative"
dict_data_bin_bundles["Name"] = "binary masks of bundle-segmentations"

#the generation is equal to tractograhy files but there is the conversion in binary masks 
dict_data_bin_bundles["GeneratedBy"].append( {
                                   "Name": "Unknown",    #!missing!
                                   "Description": "Generated tractography were converted in binary masks, indicating were the bundles pass"
                                     })
                                 



with open(path_data_description_bin_masks_json, "w") as outfile:
    json.dump(dict_data_bin_bundles, outfile)
    
    