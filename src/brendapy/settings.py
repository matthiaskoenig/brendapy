"""Paths to main resources and resource management.

Due to the size limits of git and pypi the large resources
cannot be managed/included in git and pypi.
These resources have to be loaded from online resources on
first import.
"""


from pathlib import Path
from zipfile import ZipFile

import requests
from rich.progress import Progress

from brendapy.console import console
from brendapy.log import get_logger


logger = get_logger(__name__)


BASE_PATH = Path(__file__).parent
RESOURCES_PATH = BASE_PATH / "resources"

BRENDA_FILE = RESOURCES_PATH / "data" / "brenda" / "brenda_download.txt"
TAXONOMY_ZIP = RESOURCES_PATH / "data" / "taxonomy" / "taxdmp.zip"
TAXONOMY_JSON = RESOURCES_PATH / "data" / "taxonomy" / "taxonomy.json"


def download_file(url: str, directory: Path) -> None:
    """Download resource."""

    console.print(f"Download of BRENDApy resources ({url})")
    local_filename = directory / url.split("/")[-1]
    with Progress() as progress:

        response = requests.get(url, stream=True)
        total_size_in_bytes = int(response.headers.get("content-length", 0))
        block_size = 1024
        task1 = progress.add_task("[green]Progress", total=total_size_in_bytes)
        with open(local_filename, "wb") as file:
            for data in response.iter_content(block_size):
                progress.update(task1, advance=block_size)
                file.write(data)


ZIP_FILENAME = "brendapy-data-v0.5.0.zip"
ZIP_PATH = RESOURCES_PATH / ZIP_FILENAME
if not ZIP_PATH.exists():
    url = f"http://134.176.27.178/brendapy/{ZIP_FILENAME}"
    download_file(url=url, directory=RESOURCES_PATH)
    if not ZIP_PATH.exists():
        logger.error("brendapy data could not be downloaded")
        raise IOError(f"{ZIP_PATH} does not exist.")

    # extract resources
    console.print(f"[success]Extract {ZIP_PATH}")
    with ZipFile(ZIP_PATH, "r") as zip:
        zip.extractall(RESOURCES_PATH)
