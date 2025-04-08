import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding an existing element in the list."""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 13) == 6

def test_binary_search_not_found():
    """Test searching for elements not in the list."""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1
    assert binary_search(arr, 6) == -1

def test_binary_search_empty_list():
    """Test searching in an empty list."""
    arr = []
    assert binary_search(arr, 5) == -1

def test_binary_search_single_element():
    """Test searching in a single-element list."""
    arr = [5]
    assert binary_search(arr, 5) == 0
    assert binary_search(arr, 6) == -1

def test_binary_search_invalid_input():
    """Test error handling for invalid inputs."""
    # Non-list input
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    
    # Unsorted list
    with pytest.raises(ValueError):
        binary_search([5, 2, 1, 3], 5)

def test_binary_search_duplicate_elements():
    """Test behavior with duplicate elements."""
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 5]
    # Note: returns index of first occurrence
    assert binary_search(arr, 3) in [3, 4, 5]
    assert binary_search(arr, 2) in [1, 2]
    assert binary_search(arr, 4) in [6, 7]