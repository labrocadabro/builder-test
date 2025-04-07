import pytest
from src.string_reversal import reverse_string

def test_basic_string_reversal():
    """Test basic string reversal."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"

def test_empty_string():
    """Test reversal of an empty string."""
    assert reverse_string("") == ""

def test_single_character():
    """Test reversal of a single character."""
    assert reverse_string("a") == "a"

def test_string_with_spaces():
    """Test reversal of string with spaces."""
    assert reverse_string("hello world") == "dlrow olleh"

def test_string_with_special_characters():
    """Test reversal of string with special characters."""
    assert reverse_string("a1b2c3!@#") == "#@!3c2b1a"

def test_invalid_input_type():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(None)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        reverse_string(["list"])