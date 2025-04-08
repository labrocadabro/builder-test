import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_conversion():
    """Test basic RGB to Hex conversion"""
    assert rgb_to_hex(255, 255, 255) == '#FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '#000000'
    assert rgb_to_hex(255, 0, 0) == '#FF0000'
    assert rgb_to_hex(0, 255, 0) == '#00FF00'
    assert rgb_to_hex(0, 0, 255) == '#0000FF'

def test_mixed_color_conversion():
    """Test conversion of mixed color values"""
    assert rgb_to_hex(128, 128, 128) == '#808080'
    assert rgb_to_hex(173, 216, 230) == '#ADD8E6'

def test_single_digit_padding():
    """Test that single-digit values are zero-padded"""
    assert rgb_to_hex(1, 2, 3) == '#010203'

def test_invalid_input_low():
    """Test handling of values below 0"""
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, -1, 0)
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, -1)

def test_invalid_input_high():
    """Test handling of values above 255"""
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(256, 0, 0)
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, 256)

def test_invalid_input_type():
    """Test handling of non-integer inputs"""
    with pytest.raises(TypeError, match="Red value must be an integer"):
        rgb_to_hex('255', 0, 0)
    with pytest.raises(TypeError, match="Green value must be an integer"):
        rgb_to_hex(0, '255', 0)
    with pytest.raises(TypeError, match="Blue value must be an integer"):
        rgb_to_hex(0, 0, '255')