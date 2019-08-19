import os
import zipfile
import logging

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
RESOURCES_PATH = os.path.join(BASE_PATH, 'resources')

BRENDA_FILE = os.path.join(
    RESOURCES_PATH, "brenda_download.txt"
)
