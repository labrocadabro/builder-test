import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test standard RGB to Hex conversion"""
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(128, 128, 128) == '808080'

def test_edge_cases():
    """Test edge case inputs"""
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'

def test_single_digit_padding():
    """Test that single-digit values are zero-padded"""
    assert rgb_to_hex(10, 15, 5) == '0A0F05'

def test_invalid_input_low():
    """Test handling of values below 0"""
    with pytest.raises(ValueError, match=".*must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match=".*must be between 0 and 255"):
        rgb_to_hex(0, -5, 0)
    with pytest.raises(ValueError, match=".*must be between 0 and 255"):
        rgb_to_hex(0, 0, -10)

def test_invalid_input_high():
    """Test handling of values above 255"""
    with pytest.raises(ValueError, match=".*must be between 0 and 255"):
        rgb_to_hex(256, 0, 0)
    with pytest.raises(ValueError, match=".*must be between 0 and 255"):
        rgb_to_hex(0, 300, 0)
    with pytest.raises(ValueError, match=".*must be between 0 and 255"):
        rgb_to_hex(0, 0, 500)

def test_invalid_input_type():
    """Test handling of non-integer inputs"""
    with pytest.raises(TypeError, match=".*must be an integer"):
        rgb_to_hex(1.5, 0, 0)
    with pytest.raises(TypeError, match=".*must be an integer"):
        rgb_to_hex(0, '10', 0)
    with pytest.raises(TypeError, match=".*must be an integer"):
        rgb_to_hex(0, 0, [255])