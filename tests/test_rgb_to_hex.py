import pytest
from src.rgb_to_hex import rgb_to_hex

def test_basic_rgb_to_hex():
    """Test conversion of basic RGB values"""
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(255, 0, 0) == 'FF0000'
    assert rgb_to_hex(0, 255, 0) == '00FF00'
    assert rgb_to_hex(0, 0, 255) == '0000FF'

def test_mixed_rgb_to_hex():
    """Test conversion of mixed RGB values"""
    assert rgb_to_hex(148, 0, 211) == '9400D3'
    assert rgb_to_hex(34, 139, 34) == '228B22'

def test_edge_cases():
    """Test edge case values"""
    assert rgb_to_hex(0, 0, 0) == '000000'
    assert rgb_to_hex(255, 255, 255) == 'FFFFFF'

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test values out of range
    with pytest.raises(ValueError, match="Red value must be between 0 and 255"):
        rgb_to_hex(-1, 0, 0)
    
    with pytest.raises(ValueError, match="Green value must be between 0 and 255"):
        rgb_to_hex(0, 256, 0)
    
    with pytest.raises(ValueError, match="Blue value must be between 0 and 255"):
        rgb_to_hex(0, 0, 300)
    
    # Test non-integer inputs
    with pytest.raises(TypeError, match="Red value must be an integer"):
        rgb_to_hex(1.5, 0, 0)
    
    with pytest.raises(TypeError, match="Green value must be an integer"):
        rgb_to_hex(0, '100', 0)
    
    with pytest.raises(TypeError, match="Blue value must be an integer"):
        rgb_to_hex(0, 0, [255])