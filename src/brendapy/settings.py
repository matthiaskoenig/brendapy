"""Paths to main resources and resource management.

Due to the size limits of git and pypi the large resources
cannot be managed/included in git and pypi.
These resources have to be loaded from online resources on
first import.
"""

import shutil
from pathlib import Path
from zipfile import ZipFile

import requests

from brendapy.log import get_logger


logger = get_logger(__name__)


BASE_PATH = Path(__file__).parent
RESOURCES_PATH = BASE_PATH / "resources"

BRENDA_FILE = RESOURCES_PATH / "data" / "brenda" / "brenda_download.txt"
TAXONOMY_ZIP = RESOURCES_PATH / "data" / "taxonomy" / "taxdmp.zip"
TAXONOMY_JSON = RESOURCES_PATH / "data" / "taxonomy" / "taxonomy.json"


def download_file(url: str, directory: Path):
    """Download resource."""
    local_filename = directory / url.split("/")[-1]
    logger.warning(f"Download {url}")
    with requests.get(url, stream=True) as r:
        with open(local_filename, "wb") as f:
            shutil.copyfileobj(r.raw, f)

    logger.info("Download finished")
    return local_filename


ZIP_FILENAME = "brendapy-data-v0.5.0.zip"
ZIP_PATH = RESOURCES_PATH / ZIP_FILENAME
if not ZIP_PATH.exists():
    url = f"http://141.20.66.64/brendapy/{ZIP_FILENAME}"
    download_file(url=url, directory=RESOURCES_PATH)
    if not ZIP_PATH.exists():
        logger.error("brendapy data could not be downloaded")
        raise IOError(f"{ZIP_PATH} does not exist.")

    # extract resources
    logger.warning(f"Extraction {ZIP_PATH} ...")
    with ZipFile(ZIP_PATH, "r") as zipObj:
        zipObj.extractall(RESOURCES_PATH)
    logger.warning(f"Extraction finished.")
