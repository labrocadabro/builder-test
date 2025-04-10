import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding an existing element in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6

def test_binary_search_not_found():
    """Test element not in the list"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1
    assert binary_search(arr, 6) == -1

def test_binary_search_empty_list():
    """Test searching in an empty list"""
    arr = []
    assert binary_search(arr, 5) == -1

def test_binary_search_single_element():
    """Test searching in a single-element list"""
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 6) == -1

def test_binary_search_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    
    with pytest.raises(ValueError):
        binary_search([5, 3, 1], 3)  # Unsorted list

def test_binary_search_floating_point():
    """Test binary search with floating point numbers"""
    arr = [1.1, 2.2, 3.3, 4.4, 5.5]
    assert binary_search(arr, 3.3) == 2
    assert binary_search(arr, 6.6) == -1