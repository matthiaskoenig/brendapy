# -*- coding: utf-8 -*-
import os
from zipfile import ZipFile

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

# These are distributed
RESOURCES_PATH = os.path.join(BASE_PATH, 'resources')
# These are only available in development
DATA_PATH = os.path.join(BASE_PATH, 'data')


BRENDA_FILE = os.path.join(RESOURCES_PATH, "brenda.txt")
BRENDA_ZIP = os.path.join(RESOURCES_PATH, "brenda.txt.zip")


if not os.path.exists(BRENDA_FILE):
    with ZipFile(BRENDA_ZIP, 'r') as zipObj:
        zipObj.extractall(RESOURCES_PATH)
