import pytest

from zad5 import group_files_by_extension

def test_empty_list():
    assert group_files_by_extension([]) == {}

def test_not_empty_list():

    file_names = ['xd.pl']
    expected_result = {'pl': ['xd.pl']}
    assert group_files_by_extension(file_names) == expected_result

def test_multiple_extensions():
    file_names = ['plik1.jpg', 'plik2.gif', 'plik3.mid', 'plik4.jpg', 'plik5.png']
    expected_result = {
        'jpg': ['plik1.jpg', 'plik4.jpg'],
        'gif': ['plik2.gif'],
        'mid': ['plik3.mid'],
        'png': ['plik5.png']
    }
    assert group_files_by_extension(file_names) == expected_result







if __name__ == "__main__":
    pytest.main()


