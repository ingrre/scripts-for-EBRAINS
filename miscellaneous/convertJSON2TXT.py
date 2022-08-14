# -*- coding: utf-8 -*-
"""
Created on Jul 20 15:39:23 2022

Script to convert meshview compatible JSON files to TXT file using the same colour definitions.
Text files are saved in the same folder as the original JSON files using the same file names.

This script was written for a specific set of files, but works for all meshview compatible JSON files 
as long as the folder the JSON files are stored in is correctly defined. This can be changed by modifying 
the definition of the variable "fnames".

@author: mvanswieten
"""

import os
import json
import glob

fpath = os.getcwd()

# Find all JSON files that are in the subfolders of the folders in the directory
fnames = glob.glob(fpath + "**\\**\\*.json", recursive = True)

# Open the files and add them to a list for further processing
file_list = []
for fname in fnames:
    with open(fname, 'r') as f:
        file_list.append(json.load(f))
    f.close()

# Loop over the list and process each file individually
for i in range(len(file_list)):
    exp_name = fnames[i].split("\\")[-1].split(".json")[0].split("_")[0:1]
    output_folder = "\\".join(fnames[i].split("\\")[:-1])
    print("Loading data for experiment: " + exp_name[i])
    # Extract the x, y, z coordinates for the list of "triplets". 
    for f in file_list[i]:
        
        coordinate_list = f["triplets"]

        fname_txt = f["name"] + ".txt"
        xs = coordinate_list[0::3]
        ys = coordinate_list[1::3]
        zs = coordinate_list[2::3]
        with open(os.path.join(output_folder,fname_txt), 'w') as fi:
            fi.write("RGB " + str(f["r"]) + " " + str(f["g"]) + " " + str(f["b"]))
            fi.write('\n')
            for l in range(f["count"]):
                fi.write(str(xs[l]))
                fi.write('\t')
                fi.write(str(ys[l]))
                fi.write('\t')
                fi.write(str(zs[l]))
                fi.write('\n')
