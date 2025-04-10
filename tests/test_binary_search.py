import pytest
from src.binary_search import binary_search

def test_basic_search():
    """Test basic binary search functionality"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 13) == 6
    assert binary_search(arr, 1) == 0

def test_element_not_found():
    """Test when element is not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1

def test_empty_list():
    """Test searching in an empty list"""
    assert binary_search([], 5) == -1

def test_single_element_list():
    """Test binary search in a single-element list"""
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 6) == -1

def test_multiple_occurrences():
    """Test lists with multiple occurrences of the same value"""
    arr = [1, 2, 2, 2, 3, 4, 5]
    assert binary_search(arr, 2) in [1, 2, 3]  # any of these indexes is acceptable

def test_invalid_input_type():
    """Test error handling for non-list inputs"""
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    with pytest.raises(TypeError):
        binary_search(123, 5)

def test_unsorted_list():
    """Test error handling for unsorted lists"""
    with pytest.raises(ValueError):
        binary_search([5, 3, 1, 4], 3)

def test_large_list():
    """Test binary search on a large sorted list"""
    arr = list(range(1000))
    assert binary_search(arr, 500) == 500
    assert binary_search(arr, 999) == 999
    assert binary_search(arr, 1000) == -1