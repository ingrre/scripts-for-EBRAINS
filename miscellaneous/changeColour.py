"""
Created on Mar 15 13:52:25 2022

File to change colours in existing JSON files that are compatible with Meshview
Either use the same RGB colour for all file you want to change, or specify the colours in a separate excel file, e.g. 'colours.xlsx'

This excel file should have the following structure:
    + column "fileName" : In this column the name of the files are defined (without the extension)
    + column "r" : the red part of the RGB colour [0-255]
    + column "g" : the green part of the RGB colour [0-255]
    + column "b" : the blue part of the RGB colour [0-255]   

The json file will be overwritten with using the same file name.

@author: mvanswieten
"""

import json
import glob
import os
import pandas as pd

answer = input("Are colours defined in a separate file? Yes (y) or No (n): ")

if answer == "n": 
    RGB = input("What is the RGB code you want to use (e.g. 255 0 0): ") 
    colors = {}
    colors["r"] = int(RGB.split(" ")[0])
    colors["g"] = int(RGB.split(" ")[1])
    colors["b"] = int(RGB.split(" ")[2])
elif answer == "y":
    colour_file = input("What is the file name in which the colours are defined for each json file you want to change? ")
    colors = pd.read_excel(colour_file + ".xlsx")
    expNames = colors.fileName.to_list()

cwd = os.getcwd()

experiment_files = glob.glob(os.path.join(cwd,"") + "*.json", recursive = True)

coordinateList = {}

for fname in experiment_files:
    name_exp = os.path.split(fname)[-1].split(".json")[0]
    if answer == "y": 
        for i in range(len(expNames)):
            if name_exp == str(expNames[i]):
                r = int(colors.r[i])
                g = int(colors.g[i])
                b = int(colors.b[i])
    else:
        r = int(colors["r"])
        g = int(colors["g"])
        b = int(colors["b"])

    with open(fname, 'r') as f:
        coordinateList[name_exp] = json.load(f)

        file = coordinateList[name_exp]
        for ii in range(len(file)):
            file[ii]["r"] = r
            file[ii]["g"] = g
            file[ii]["b"] = b

        with open(fname, 'w', encoding='utf-8') as fi:
            fi.write(json.dumps(file, ensure_ascii=False, indent=4))
    
    f.close()
