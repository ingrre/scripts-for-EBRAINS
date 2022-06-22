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

### Advanced Curation
1. ``make_protocols.ipynb :`` script to automatically create protocols and protocol executions from an excel template file (protocolTemplate.xlsm). The instances rely on the openMINDS python package and are openMINDS conform. They can be directly uploaded to the Knowledge Graph editor if you have read and write permission. Relevant information is stored in a csv file with the name "createdProtocols.csv"
2. ``protocolTemplate.xlsm :`` Macro-enabled excel file for the creation of protocols and protocol executions (don't forget to enable the macros). Before running the jupyter notebook, please save the file as an .xlsx file. This will disable the macros and allows it to be imported by the python script.
