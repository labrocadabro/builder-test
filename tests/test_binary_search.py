import pytest
from src.binary_search import binary_search

def test_binary_search_normal_case():
    """Test binary search with a typical sorted list of integers"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6

def test_binary_search_not_found():
    """Test when target is not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 4) is None
    assert binary_search(arr, 0) is None
    assert binary_search(arr, 14) is None

def test_binary_search_empty_list():
    """Test binary search on an empty list"""
    arr = []
    assert binary_search(arr, 5) is None

def test_binary_search_single_element():
    """Test binary search with a single-element list"""
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 4) is None

def test_binary_search_duplicate_elements():
    """Test binary search with a list containing duplicate elements"""
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    assert binary_search(arr, 3) in [3, 4, 5]

def test_binary_search_unsorted_list():
    """Test that an unsorted list raises a TypeError"""
    arr = [5, 3, 1, 7, 2]
    with pytest.raises(TypeError, match="Input list must be sorted"):
        binary_search(arr, 3)

def test_binary_search_string_list():
    """Test binary search with a sorted list of strings"""
    arr = ['apple', 'banana', 'cherry', 'date']
    assert binary_search(arr, 'banana') == 1
    assert binary_search(arr, 'grape') is None

def test_binary_search_float_list():
    """Test binary search with a sorted list of floats"""
    arr = [1.1, 2.2, 3.3, 4.4, 5.5]
    assert binary_search(arr, 3.3) == 2
    assert binary_search(arr, 6.6) is None