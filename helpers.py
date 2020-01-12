import os

RAW_DATA = "data/raw/"
PROCESSED_DATA = "data/processed/"
FIGURES = "figures"


def find_files(directory_path: str, file_type: str = ".csv"):
    """search directory for specific file types.

    Parameters
    ----------
    directory_path : str
        path to files
    file_type: str
        type of file to load

    Returns
    -------
    files: list
        list of files that end with file_type
    """
    files = []
    for file in os.listdir(directory_path):
        if file.endswith(file_type):
            files.append(os.path.join(directory_path, file))
    return files
