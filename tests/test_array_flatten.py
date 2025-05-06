import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_nested_array():
    """Test flattening a simple nested array"""
    input_arr = [1, [2, 3], 4]
    assert flatten_array(input_arr) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array"""
    input_arr = [1, [2, [3, 4]], [5, [6, 7]]]
    assert flatten_array(input_arr) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_flatten_no_nesting():
    """Test flattening an array with no nesting"""
    input_arr = [1, 2, 3, 4, 5]
    assert flatten_array(input_arr) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types():
    """Test flattening an array with mixed types"""
    input_arr = [1, [2, 'three'], [4, [5.0, 6]]]
    assert flatten_array(input_arr) == [1, 2, 'three', 4, 5.0, 6]

def test_flatten_nested_empty_arrays():
    """Test flattening an array with nested empty arrays"""
    input_arr = [1, [], [2, []], 3]
    assert flatten_array(input_arr) == [1, 2, 3]

def test_flatten_complex_nesting():
    """Test flattening a complex nested array structure"""
    input_arr = [1, [2, [3, [4]]], 5]
    assert flatten_array(input_arr) == [1, 2, 3, 4, 5]