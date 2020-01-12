import subprocess
from helpers import RAW_DATA, PROCESSED_DATA, find_files, FIGURES


def test_find_csv_files():
    files = find_files(RAW_DATA)
    assert isinstance(files, list)
    assert files


def test_directories():
    assert isinstance(RAW_DATA, str)
    assert isinstance(PROCESSED_DATA, str)


def test_make_notebook():
    subprocess.run(["make", "notebook"])
    figures = find_files(FIGURES, '.html')
    assert figures
    processed_files = find_files(PROCESSED_DATA, '.gzip')
    assert processed_files
