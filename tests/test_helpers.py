from helpers import RAW_DATA, PROCESSED_DATA, find_files


def test_find_csv_files():
    files = find_files(RAW_DATA)
    assert isinstance(files, list)
    assert len(files) >= 1

def test_directories():
    assert isinstance(RAW_DATA, str)
    assert isinstance(PROCESSED_DATA, str)