import pytest
from src.unique_substrings import find_unique_substrings

def test_find_unique_substrings_basic():
    """Test basic substring generation"""
    result = find_unique_substrings("abc")
    assert result == ['a', 'b', 'c', 'ab', 'bc', 'abc']

def test_find_unique_substrings_empty_string():
    """Test empty string input"""
    result = find_unique_substrings("")
    assert result == []

def test_find_unique_substrings_repeated_chars():
    """Test string with repeated characters"""
    result = find_unique_substrings("aaa")
    assert result == ['a', 'aa', 'aaa']

def test_find_unique_substrings_order_preservation():
    """Test that substrings are ordered by first appearance"""
    result = find_unique_substrings("abcab")
    expected = ['a', 'b', 'c', 'ab', 'bc', 'abc', 'cab']
    assert result == expected

def test_find_unique_substrings_invalid_input():
    """Test that TypeError is raised for non-string input"""
    with pytest.raises(TypeError, match="Input must be a string"):
        find_unique_substrings(123)
        find_unique_substrings(None)
        find_unique_substrings([])