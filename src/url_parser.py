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
        # Initialize default variables
        original_scheme = None
        original_netloc = ''

        # If no scheme is present, prepend 'http://' for proper parsing
        if '://' not in url:
            parsed_url = urlparse('http://' + url)
            original_scheme = None
        else:
            parsed_url = urlparse(url)
            original_scheme = parsed_url.scheme

        # Extract query parameters using parse_qs
        query_params = parse_qs(parsed_url.query)
        
        # Flatten single-item lists in query parameters
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

        # Determine the path
        if '://' not in url:
            # For URLs without scheme, adjust path
            parts = url.split('/')
            path = '/' + '/'.join(parts[1:]) if len(parts) > 1 else None
        else:
            path = parsed_url.path or None

        # Determine netloc
        if '://' not in url:
            # For URLs without scheme, set netloc to empty string
            original_netloc = ''
        else:
            original_netloc = parsed_url.netloc

        # Construct and return a comprehensive URL information dictionary
        return {
            'scheme': original_scheme,
            'netloc': original_netloc,
            'path': path,
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