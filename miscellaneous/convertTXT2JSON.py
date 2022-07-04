"""
Created on Mar 15 13:52:25 2022

File to convert coordinates from a tab separated txt file to a JSON file compatible with Meshview
If RBG colour is defined in the txt file, this colour is used for the JSON file, otherwise the colour is set to black

example txt file input:
RGB 0 1 0

23.5 356.2 231
79,2 124   211

@author: mvanswieten
"""

import json
import glob
import os

cwd = os.getcwd()
experiment_files = glob.glob(os.path.join(cwd,"") + "*.txt", recursive = True)

for f in range(len(experiment_files)):
    
    triplets = []
    with open(experiment_files[f], "r") as my_file:
        
        for line in my_file:

            # If the RGB colour is defined on the first line of the txt file in the format RGB 0 0 0, use those colours
            if "RGB" in line: 
                currentline = line.split(" ")

                r = float(currentline[1])
                g = float(currentline[2])
                b = float(currentline[3].split("\n")[0])
            
            # Only consider lines that have text on them
            elif not line == "\n":
                currentline = line.split(",")
                coordinates = currentline[0].split("\t")

                triplets.append(float(coordinates[0]))
                triplets.append(float(coordinates[1]))   
                triplets.append(float(coordinates[2].split("\n")[0]))

                # set default colour to black
                r = 0
                g = 0
                b = 0
    
        fname = os.path.split(experiment_files[f])[-1].split(".txt")[0]
        instance = {
            "idx": 0,
            "count": int(len(triplets)/3),
            "r": int(r*255),
            "g": int(g*255),
            "b": int(b*255),
            "name": fname.split("_")[1:],
            "triplets": triplets
            }
        
        filename = fname + ".json"
        with open(filename, 'w', encoding='utf-8') as fi:
            fi.write(json.dumps([instance], ensure_ascii=False, indent=4))