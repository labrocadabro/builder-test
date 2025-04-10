from urllib.parse import urlparse, parse_qs
from typing import Dict, Any


def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL and extract its components.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components.

    Raises:
        ValueError: If the URL is invalid or empty.
    """
    # Check for empty or None URL
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # If no scheme is present, prepend 'http://' for proper parsing
        if '://' not in url:
            url = 'http://' + url

        # Use urlparse to break down the URL
        parsed_url = urlparse(url)

        # Extract query parameters using parse_qs
        query_params = parse_qs(parsed_url.query)
        
        # Flatten single-item lists in query parameters
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

        # Determine the path, removing the automatically added 'http://' if it was prepended
        path = parsed_url.path
        if not parsed_url.scheme and parsed_url.path.startswith('/http://'):
            path = parsed_url.path.replace('/http://', '/', 1)

        # Construct and return a comprehensive URL information dictionary
        return {
            'scheme': None if not parsed_url.scheme or parsed_url.scheme == 'http' else parsed_url.scheme,
            'netloc': parsed_url.netloc or None,
            'path': path or None,
            'params': parsed_url.params or None,
            'query': query_params,
            'fragment': parsed_url.fragment or None,
            'username': parsed_url.username,
            'password': parsed_url.password,
            'hostname': parsed_url.hostname,
            'port': parsed_url.port
        }
    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")