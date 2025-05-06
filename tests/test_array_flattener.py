import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list."""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_single_element():
    """Test flattening a single non-list element."""
    assert flatten_array(42) == [42]

def test_flatten_mixed_elements():
    """Test flattening a list with mixed types and nesting."""
    assert flatten_array([1, 'a', [2, [3]], {'key': 'value'}]) == [1, 'a', 2, 3, {'key': 'value'}]

def test_nested_empty_lists():
    """Test flattening nested empty lists."""
    assert flatten_array([[], [[], []]]) == []

def test_complex_nested_structure():
    """Test a more complex nested structure."""
    complex_list = [1, [2, 3], [], [4, [5, [6]]], 7]
    assert flatten_array(complex_list) == [1, 2, 3, 4, 5, 6, 7]