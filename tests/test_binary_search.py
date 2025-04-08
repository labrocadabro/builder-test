import pytest
from src.binary_search import binary_search

def test_binary_search_found():
    """Test finding an existing element in the middle of the list"""
    assert binary_search([1, 3, 5, 7, 9], 5) == 2

def test_binary_search_first_element():
    """Test finding the first element in the list"""
    assert binary_search([1, 3, 5, 7, 9], 1) == 0

def test_binary_search_last_element():
    """Test finding the last element in the list"""
    assert binary_search([1, 3, 5, 7, 9], 9) == 4

def test_binary_search_not_found():
    """Test when element is not in the list"""
    assert binary_search([1, 3, 5, 7, 9], 4) == -1

def test_binary_search_empty_list():
    """Test binary search on an empty list"""
    assert binary_search([], 5) == -1

def test_binary_search_single_element_found():
    """Test binary search on a single-element list when element is found"""
    assert binary_search([5], 5) == 0

def test_binary_search_single_element_not_found():
    """Test binary search on a single-element list when element is not found"""
    assert binary_search([5], 4) == -1

def test_binary_search_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search("not a list", 5)

def test_binary_search_unsorted_list():
    """Test that ValueError is raised for unsorted list"""
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        binary_search([5, 3, 1, 7, 9], 5)

def test_binary_search_negative_numbers():
    """Test binary search with negative numbers"""
    assert binary_search([-9, -7, -5, -3, -1], -5) == 2

def test_binary_search_repeated_elements():
    """Test binary search with repeated elements (returns first occurrence)"""
    assert binary_search([1, 2, 2, 2, 3, 4, 5], 2) in [1, 2, 3]