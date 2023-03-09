# README

The BrainPTM2021 dataset is provided by the platform https://grand-challenge.org/ and can be downloaded from https://brainptm-2021.grand-challenge.org/.
This dataset is not originally in BIDS format. After having downloaded the zip folders from https://brainptm-2021.grand-challenge.org/ can be converted into BIDS format using the code in xxxxxx.

The data are intended to be downloaded to participate in a challenge. 
The challenge consists in automatically segmenting with the highest performance possible the white matter tracts Corticospinal tract left and right and
Optic Radiation left and right in a group of glioma patients. The performance to rank the participants in the challenge is evaluated with the Dice Score Coefficient.

The dataset is composed of data concerning 75 glioma patients. Glioma patients can belong to two exclusive groups:

* the train set: subjects' data belonging to this group should be used to train an automatic algorithm to segment the white matter tracts. For these subjects, the ground truth segmentation of the tracts is provided, as tractography and binary masks.

* the test set: subjects' data beloging to this group should be used for inference by participants to the challenge, i.e. for segmenting the tracts Corticospinal tract and
Optic Radiation left and right. The predicted segmentations should be submitted to the challenge to participate. For this reason, for this subjects, the ground truth segmentation of the tracts is not provided.



## Details related to access to the data

### Data user agreement

"Participants cannot share the data, cannot use it for any commercial purpose. If this dataset or part of it is used in a published
paper (as well as test set evaluation results from the leaderboard) please cite the following papers:

@article{avital2019neural,
  title={Neural Segmentation of Seeding ROIs (sROIs) for Pre-Surgical Brain Tractography},
  author={Avital, Itzik and Nelkenbaum, Ilya and Tsarfaty, Galia and Konen, Eli and Kiryati, Nahum and Mayer, Arnaldo},
  journal={IEEE transactions on medical imaging},
  volume={39},
  number={5},
  pages={1655--1667},
  year={2019},
  publisher={IEEE}
}

@inproceedings{nelkenbaum2020automatic,
  title={Automatic Segmentation of White Matter Tracts Using Multiple Brain MRI Sequences},
  author={Nelkenbaum, Ilya and Tsarfaty, Galia and Kiryati, Nahum and Konen, Eli and Mayer, Arnaldo},
  booktitle={2020 IEEE 17th International Symposium on Biomedical Imaging (ISBI)},
  pages={368--371},
  year={2020},
  organization={IEEE}
}"[2]


### Contacts 

"The challenge is organized by the CILAB@Sheba medical center, Israel"[1].

Link to the CILAB group: https://www.cilab.org.il/


For any questions about the data on the [website](https://brainptm-2021.grand-challenge.org/) [2] are indicated the persons that you can contact:

* Ilya Nelkenbaum, Computational Imaging Lab (CILAB), Tel-Hashomer, Ramat Gan, Israel; email: ilya@nelkenbaum.com
* Noa Barzilay, Computational Imaging Lab (CILAB), Tel-Hashomer, Ramat Gan, Israel; email: noabarzilay11@gmail.com
* Arnaldo Mayer, Head of Computational Imaging Lab (CILAB), Tel-Hashomer, Ramat Gan, Israel; email : arnmayer@gmail.com[2]
  

### Practical information to access the data
The data can be downloaded from https://brainptm-2021.grand-challenge.org/, after joining the challenge.
The zip folders downloaded from https://brainptm-2021.grand-challenge.org/ can be converted in BIDS format using code in xxxx.

 

## Overview


## Methods

### Subjects

"The dataset used for the experiments consists of image data from 75 patients referred for brain tumor removal (..). Patient diagnoses include oligodendrogliomas, astrocytomas, glioblastomas and cavernomas, on first occurrence or in a post-surgical recurrence. The patients underwent pre-surgical DTI mapping of the motor, language, visual, or a combination of those tracts, depending on their proximity to the lesion. According to the neuroradiologist’s estimation, the tumor volumes ranged from 4 (cavernoma) to 60 cm3 (glioblastoma multiforme). Also, different levels of edema are present around the dataset tumors."[1]



### Apparatus
"The dataset comprises 75 clinical cases with T1w Structural and Diffusion Weighted (DW) modalities.
The scans were acquired on a 3T Signa machine (GE healthcare, Milwaukee). The DW protocol had 64
gradient directions at B0 = 1000 and one scan at B0 = 0. T1w with no contrast injection was acquired at
1x1x1 mm^3 resolution and the DW with 1x1x2.6 mm^3. DW was processed with MrDiffusion toolbox [3]
for Matlab and registered to the high resolution T1w. Finally T1w scans were skull stripped with BET [4] and
resliced to 1.25x1.25x1.25 mm^3, DW scans (registered to T1w) were resliced to 1.25x1.25x1.25 mm^3 as well.
Each T1w and DW scan is stored in a separate nifti file with 128x144x128 spatial dimension.

White matter tracts mapping annotations were acquired in a semi-manual process for each scan. Optic Radiation (OR)
and Corticospinal tracts (CST) (left and right) were chosen as they are of significant interest during neuro-surgical planning.

Tracts annotations are provided only for 60 cases (train set) while the rest 15 cases are used for participants
algorithms evaluation, so only the input cases scans are provided (T1w and DW)."[2]



### Experimental location

The data were acquired at Sheba Medical Center in Tel HaShomer, Israel.


### Missing data
"NOTE: for 4 out of the 60 train cases there are no CST tracts annotations, due to difficulties in tractography reconstruction."[2]



## References:

[1]Avital, Itzik, Ilya Nelkenbaum, Galia Tsarfaty, Eli Konen, Nahum Kiryati, and Arnaldo Mayer. “Neural Segmentation of Seeding ROIs (SROIs) for Pre-Surgical Brain Tractography.” IEEE Transactions on Medical Imaging 39, no. 5 (May 2020): 1655–67. https://doi.org/10.1109/TMI.2019.2954477.

[2]grand-challenge.org. “BrainPTM 2021 - Grand Challenge.” Accessed August 29, 2022. https://brainptm-2021.grand-challenge.org/.

[3]“MrDiffusion - VISTA LAB WIKI.” Accessed March 2, 2023. https://web.stanford.edu/group/vista/cgi-bin/wiki/index.php/MrDiffusion.

[4]M. Jenkinson, M. Pechaud, and S. Smith. BET2: MR-based estimation of brain, skull and scalp surfaces. In Eleventh Annual Meeting of the Organization for Human Brain Mapping, 2005.

