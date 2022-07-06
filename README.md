# scripts-for-EBRAINS

This repository contains some python scripts and jupyter notebooks specifically made for the use of EBRAINS related curation and optimisation.

## Requirements

To run the scripts, the following requirements apply:
1. Python version 3.6 or higher
2. openMINDS python package [(can be downloaded from PyPi)](https://pypi.org/project/openMINDS/)
3. Authorisation to read and write to the Knowledge Graph via the API

## Contents

### Image Service
1. ``link_filebundles.ipynb :`` script to automatically link specimen to their corresponding file bundles. Relevant information is stored in a csv file with the name "fb_<dataset version uuid>"
2. ``extract_tsc_info.ipynb :`` script to extract important metadata related to a tissue sample collection. This information is stored in a csv file with the name "tsc_<dataset version uuid>"
3. ``create_servicelinks.ipynb :`` script to create URL and service link instances based on the provided metadata. These instances can be directly uploaded to the KG editor via the API.

### Curation
**Creating Protocols and Protocol Executions**
1. ``make_protocols.ipynb :`` script to automatically create protocols and protocol executions from an excel template file (protocolTemplate.xlsm). The instances rely on the openMINDS python package and are openMINDS conform. They can be directly uploaded to the Knowledge Graph editor if you have read and write permission. Relevant information is stored in a csv file with the name "createdProtocols.csv".
2. ``protocolTemplate.xlsm :`` Macro-enabled excel file for the creation of protocols and protocol executions (don't forget to enable the macros). Before running the jupyter notebook, please save the file as an .xlsx file. This will disable the macros and allows it to be imported by the python script.

**Changing existing metadata for specimen**
1. ``patchNupload.ipynb :`` script to add/change metadata from an excel file (e.g. ExamplePatch.xlsx) to existing specimen instances in the KGE.
2. ``ExamplePatch.xlsx :`` Example excel file to define metadata and update instances.

**Creating Persons**
1. ``create_persons.ipynb :`` script to create persons (first name, last name, email address and ORCID) from excel file (e.g. personTemplate.xlsx) and upload instances to the correct space in the KGE (common for person and ORCID and restricted for email address). Relevant information is stored in a csv file with the name "createdPersons.csv".
2. ``personTemplate.xlsx :`` Example excel file to define person metadata.

**Releasing instances**
1. ``release_instance :`` script to release instances based on the uuid. You can either list the uuids you want to release in an excel file (e.g. instances2release.xlsx), or you can paste an individual uuid in the script (when asked the questions).
2. ``instances2release.xlsx :`` Example excel file for releasing multiple instances at the same time.

### Miscellaneous
**MeshView related**
1. ``changeColour.py :`` script to change colours in a MeshView compatible JSON file. Colours can be individually defined in an excel file where the filename and corresponding colour is defined on each row in the excel file, or one colour can be defined for all files at the start of the script (as answer to one of the questions).
2. ``convertTXT2JSON.py :`` script to convert coordinates in a text file to a MeshView compatible JSON file. Coordinates in the txt file should be tab-separated. Each line represent x y z coordinates. The colour of the coordinates can be defined on the first row of the txt file using the RGB code, e.g. RGB 0 0 255. If no RGB code is defined, the colour is set to black as default.
3. ``exportCoordinates.py :`` script to export coordinates from a MeshView compatible JSON file and save them in a csv file.
