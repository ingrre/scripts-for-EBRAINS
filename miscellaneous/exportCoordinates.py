# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 16:39:23 2022

Script to extract x,y,z coordinates from a JSON file generated for the use of Meshview

Place the script in the target folder with the JSON file (or define the folder instead of cwd). 
It will extract coordinates for all json files in the folder and saves the x,y,z coordinates in a csv file.

@author: mvanswieten
"""

import os
import json
import glob
import pandas as pd

fpath = os.getcwd()
fnames = glob.glob(os.path.join(fpath,"") + "*.json", recursive = True)

file_list = []
for fname in fnames:
    with open(fname, 'r') as f:
        file_list.append(json.load(f))
    f.close()

# Interate over all json files found in the target folder
for i in range(len(file_list)):
    exp_name = os.path.split(fnames[i])[-1].split(".json")[0]
    print("Loading data for experiment: " + str(exp_name))
    
    # Iterate over the nested objects in the json file
    for f in file_list[i]:

        coordinate_list = f["triplets"]

        print("Extracting coordinates for: " + f["name"])
        
        # The MeshView JSON files are saved as triplets. We therefore need to select every 3rd element for the x, y and z coordinates
        d = {
             "x_coordinate" : coordinate_list[0::3], 
             "y_coordinate" : coordinate_list[1::3], 
             "z_coordinate" : coordinate_list[2::3]
             }
        
        data = pd.DataFrame(d)

        # Save output file in the current working directory (target folder) as a csv file
        print("Saving coordinate file")
        if len(file_list[i]) > 1:
            new_fname = exp_name + "_" + f["name"].strip() + ".csv"
        else:
            new_fname = exp_name + ".csv"
        data.to_csv(new_fname, index = False, header=True)
        
