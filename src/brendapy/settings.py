# -*- coding: utf-8 -*-
"""
Paths to main resources and resource management.

Due to the size limits of git and pypi the large resources
cannot be managed/included in git and pypi.
These resources have to be loaded from online resources on
first import.

"""
import os
import logging
from zipfile import ZipFile

import requests
import shutil

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
RESOURCES_PATH = os.path.join(BASE_PATH, 'resources')

BRENDA_FILE = os.path.join(RESOURCES_PATH, "data", "brenda", "brenda_download.txt")
TAXONOMY_DATA = os.path.join(RESOURCES_PATH, "data", "taxonomy", "taxonomy.json")
TAXONOMY_ZIP = os.path.join(RESOURCES_PATH, "data", "taxonomy", "taxdmp.zip")
BTO_DATA = os.path.join(RESOURCES_PATH, "data", "bto", "bto.json")
CHEBI_DATA = os.path.join(RESOURCES_PATH, "data", "chebi", "chebi.json")


# ------------------------------------------------
# Download resources
# ------------------------------------------------
def download_file(url, directory):
    local_filename = os.path.join(directory, url.split('/')[-1])
    logging.warning(f"Download {url}")
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    logging.warning(f"Download finished")
    return local_filename


ZIP_FILENAME = "brendapy-data-v0.4.0.zip"
ZIP_PATH = os.path.join(RESOURCES_PATH, ZIP_FILENAME)
if not os.path.exists(ZIP_PATH):
    url = f"http://141.20.66.64/brendapy/{ZIP_FILENAME}"
    download_file(url=url, directory=RESOURCES_PATH)
    if not os.path.exists(ZIP_PATH):
        logging.error("brendapy data could not be downloaded")
        raise IOError(f"{ZIP_PATH} does not exist.")

    # extract resources
    logging.warning(f"Extraction {ZIP_PATH} ...")
    with ZipFile(ZIP_PATH, 'r') as zipObj:
        zipObj.extractall(RESOURCES_PATH)
    logging.warning(f"Extraction finished.")
# ------------------------------------------------
