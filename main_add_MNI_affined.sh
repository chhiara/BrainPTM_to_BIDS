#!/bin/bash

cd add_MNI_affined

#1. copy MNI registered files for train cases
python cp_regMNI_train.py

#2. copy MNI registered files for test cases
python cp_regMNI_test.py