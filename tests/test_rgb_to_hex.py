import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to Hex conversion"""
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(255, 0, 0) == 'FF0000'
    assert rgb_to_hex(0, 255, 0) == '00FF00'
    assert rgb_to_hex(0, 0, 255) == '0000FF'

def test_mid_range_colors():
    """Test mid-range color conversions"""
    assert rgb_to_hex(128, 128, 128) == '808080'
    assert rgb_to_hex(76, 175, 80) == '4CAF50'

def test_zero_padding():
    """Ensure single-digit hex values are zero-padded"""
    assert rgb_to_hex(1, 2, 3) == '010203'

def test_invalid_input_low():
    """Test handling of values below 0"""
    with pytest.raises(ValueError, match="RGB values must be integers between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="RGB values must be integers between 0 and 255"):
        rgb_to_hex(0, -10, 0)
    with pytest.raises(ValueError, match="RGB values must be integers between 0 and 255"):
        rgb_to_hex(0, 0, -255)

def test_invalid_input_high():
    """Test handling of values above 255"""
    with pytest.raises(ValueError, match="RGB values must be integers between 0 and 255"):
        rgb_to_hex(256, 0, 0)
    with pytest.raises(ValueError, match="RGB values must be integers between 0 and 255"):
        rgb_to_hex(0, 300, 0)
    with pytest.raises(ValueError, match="RGB values must be integers between 0 and 255"):
        rgb_to_hex(0, 0, 500)