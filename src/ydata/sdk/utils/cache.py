from pathlib import Path
from urllib import request


def get_project_root() -> Path:
    """Returns the path to the project root folder.
    Returns:
        The path to the project root folder.
    """
    return Path(__file__).parent.parent.parent.parent.parent


def get_data_path() -> Path:
    """Returns the path to the dataset cache ([root] / data)
    Returns:
        The path to the dataset cache
    """
    return get_project_root() / "examples" / "data"


def cache_file(file_name: str, url: str) -> Path:
    """Check if file_name already is in the data path, otherwise download it from url.
    Args:
        file_name: the file name
        url: the URL of the dataset
    Returns:
        The relative path to the dataset
    """

    data_path = get_data_path()
    data_path.mkdir(exist_ok=True)

    file_path = data_path / file_name

    # If not exists, download and create file
    if not file_path.exists():
        response = request.urlopen(url)
        file_path.write_bytes(response.read())

    return file_path
