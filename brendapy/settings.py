import os
import zipfile
import logging

BASE_PATH = os.path.dirname(os.path.realpath(__file__))
RESOURCES_PATH = os.path.join(BASE_PATH, 'resources')

BRENDA_FILE = os.path.join(
    RESOURCES_PATH, "brenda_download.txt"
)


# BRENDA_FILE_ZIP = os.path.join(
#     RESOURCES_PATH, "brenda_download_2019-07-29.zip"
# )
# if not os.path.exists(BRENDA_FILE):
#     with zipfile.ZipFile(BRENDA_FILE_ZIP, 'r') as zip_obj:
#         zip_obj.extractall(RESOURCES_PATH)
#         logging.info("BRENDA file extracted")
