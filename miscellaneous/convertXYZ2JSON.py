"""
Created on Jul 20 13:52:25 2022

Script to convert coordinates from a .xyz file to a JSON file compatible with Meshview

This script was written for a specific set of files, but works for all .xyz files as long 
as the folder the .xyz files are stored in is correctly defined. This can be changed by modifying 
the definition of the variable "experiment_files". 

The colour used for the JSON file is dependent on the type of injection tracer. BDA/PHA/WGA is 
black, Fe/FE is green, Fr is red, FG is yellow, and FB is blue. If the files do not follow the 
naming convention of the files the script was written for, then the colour of the points is set 
to black by default.

@author: mvanswieten
"""

import json
import glob
import os

cwd = os.getcwd()

# Find all JSON files that are in the subfolders of the folders in the directory
experiment_files = glob.glob(os.path.join(cwd,"") + "**\\**\\*.xyz", recursive = True)

output_path = os.path.join(cwd,"output_files")

for f in range(len(experiment_files)):
    
    triplets = []
    with open(experiment_files[f], "r") as my_file:
        output_folder = os.path.join(output_path, "\\".join(experiment_files[f].split("\\")[-3:-1]), "")
        if not os.path.isdir(output_folder):
            os.makedirs(output_folder)

        if experiment_files[f].split("\\")[-2] in ["BDA", "PHA", "WGA"]:
                r = 0
                g = 0
                b = 0
        elif experiment_files[f].split("\\")[-2] in ["Fe", "FE"]:
                r = 0
                g = 0.5
                b = 0
        elif experiment_files[f].split("\\")[-2] == "Fr" :
                r = 1
                g = 0
                b = 0
        elif experiment_files[f].split("\\")[-2] == "FG":
                r = 1
                g = 1
                b = 0
        elif experiment_files[f].split("\\")[-2] == "FB":
                r = 0
                g = 0
                b = 1
        else:
                r = 0
                g = 0
                b = 0

        for line in my_file:

            # Skip the lines with a hashtag
            if "#" in line: 
                continue
            # Only consider lines that have text/coordinates on them
            elif not line == "\n":
                currentline = line.split(",")
                if len(currentline[0].split(" ")) == 3:
                    coordinates = currentline[0].split(" ")
                else:
                    coordinates = currentline[0].split("\t")

                triplets.append(float(coordinates[0]))
                triplets.append(float(coordinates[1]))   
                triplets.append(float(coordinates[2].split("\n")[0]))
    
        fname = os.path.split(experiment_files[f])[-1].split(".xyz")[0]
        instance = {
            "idx": 0,
            "count": int(len(triplets)/3),
            "r": int(r*255),
            "g": int(g*255),
            "b": int(b*255),
            "name": ("_").join(fname.split("_")[2:4]),
            "triplets": triplets
            }
        
        # Save the file using the original name and organisation in a new output folder
        filename = ("_").join(fname.split("_")[2:4]) + ".json"
        with open(os.path.join(output_folder,filename), 'w', encoding='utf-8') as fi:
            fi.write(json.dumps([instance], ensure_ascii=False, indent=4))