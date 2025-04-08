import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding elements that exist in the list"""
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 9) == 4

def test_binary_search_not_found():
    """Test searching for elements not in the list"""
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([1, 3, 5, 7, 9], 0) == -1
    assert binary_search([1, 3, 5, 7, 9], 10) == -1

def test_binary_search_empty_list():
    """Test searching in an empty list"""
    assert binary_search([], 5) == -1

def test_binary_search_single_element():
    """Test searching in a single-element list"""
    assert binary_search([5], 5) == 0
    assert binary_search([5], 6) == -1

def test_binary_search_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    with pytest.raises(TypeError):
        binary_search(None, 5)

def test_binary_search_unsorted_list():
    """Test error handling for unsorted lists"""
    with pytest.raises(ValueError):
        binary_search([5, 3, 1, 9, 7], 5)

def test_binary_search_large_list():
    """Test binary search on a larger sorted list"""
    large_list = list(range(0, 1000, 2))  # Even numbers from 0 to 998
    assert binary_search(large_list, 500) == large_list.index(500)
    assert binary_search(large_list, 501) == -1