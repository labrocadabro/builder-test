import pytest
from src.url_parser import parse_url


def test_basic_url_parsing():
    """Test parsing a basic URL with all components."""
    url = "https://www.example.com/path?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'www.example.com'
    assert result['path'] == '/path'
    assert result['query'] == {'key1': 'value1', 'key2': 'value2'}
    assert result['fragment'] == 'fragment'


def test_url_with_authentication():
    """Test URL with username and password."""
    url = "https://username:password@example.com"
    result = parse_url(url)
    
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['hostname'] == 'example.com'


def test_url_with_port():
    """Test URL with a specific port."""
    url = "http://example.com:8080/path"
    result = parse_url(url)
    
    assert result['port'] == 8080
    assert result['scheme'] == 'http'


def test_complex_query_params():
    """Test URL with multiple values for a single query parameter."""
    url = "https://example.com/search?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result['query'] == {'tag': ['python', 'programming']}


def test_invalid_url_error():
    """Test error handling for invalid URLs."""
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("")
    
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url(None)


def test_minimal_url():
    """Test parsing a minimal URL."""
    url = "https://example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'example.com'
    assert result['path'] is None


def test_url_without_scheme():
    """Test URL without a scheme."""
    url = "example.com/path"
    result = parse_url(url)
    
    assert result['scheme'] is None
    assert result['path'] == '/path'
    assert result['netloc'] == ''