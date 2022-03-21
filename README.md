# scripts-for-EBRAINS

This repository contains some python scripts and jupyter notebooks specifically made for the use of EBRAINS related curation and optimisation.

## Requirements

To run the scripts, the following requirements apply:
1. Python version 3.6 or higher
2. openMINDS python package [(can be downloaded from PyPi)](https://pypi.org/project/openMINDS/)
3. Authorisation to read and write to the Knowledge Graph via the API

## Contents

### imageservice
1. ``extract_tsc_info.ipynb :`` script to extract important metadata related to a tissue sample collection. This information is stored in a csv file with the name "tsc_<dataset version uuid>"
2. ``create_servicelinks.ipynb :`` script to create URL and service link instances based on the provided metadata. These instances can be directly uploaded to the KG editor via the API.
