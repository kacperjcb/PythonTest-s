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

def test_group_files_by_extension_no_extension():
    file_names = ["plik1", "plik2", "plik3"]
    result = group_files_by_extension(file_names)
    assert "" in result
    assert len(result[""]) == len(file_names)

def test_group_files_by_extension_invalid_names():
    file_names = ["plik1.jpg", "plik2.", ".plik3", "plik4"]
    result = group_files_by_extension(file_names)
    assert "" in result
    assert len(result[""]) == 2

def test_group_files_by_extension_spaces_in_names():
    file_names = ["plik 1.jpg", "plik 2.gif", "plik 3.mid", "plik 4.jpg"]
    result = group_files_by_extension(file_names)
    assert "" not in result
    assert "jpg" in result
    assert "gif" in result
    assert "mid" in result





if __name__ == "__main__":
    pytest.main()


