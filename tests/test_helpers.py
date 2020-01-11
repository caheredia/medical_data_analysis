from helpers import RAW_DATA, TRANSFORMED_DATA, find_csv_files


def test_find_csv_files():
    files = find_csv_files(RAW_DATA)
    assert isinstance(files, list)
    assert len(files) >= 1
