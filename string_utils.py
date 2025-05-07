# Improved string_utils module

def reverse_string(s: str) -> str:
    """
    Return the reversed version of a string.
    Args:
        s (str): input string
    Returns:
        str: reversed string
    """
    return s[::-1]

def sanitize_input(s: str) -> str:
    """
    Remove potentially unsafe characters from input.
    Args:
        s (str): input string
    Returns:
        str: cleaned string
    """
    import re
    return re.sub(r'[^\w\s\-]', '', s)

def to_title_case(s: str) -> str:
    """
    Convert input to title case.
    """
    return s.title()

def strip_whitespace(s: str) -> str:
    """
    Strip leading and trailing spaces.
    """
    return s.strip()

def run(action: str, value: str) -> str:
    """
    Dispatch string utility based on action.
    """
    try:
        if action == 'reverse':
            return reverse_string(value)
        elif action == 'sanitize':
            return sanitize_input(value)
        elif action == 'title':
            return to_title_case(value)
        elif action == 'strip':
            return strip_whitespace(value)
        else:
            return 'Unknown action'
    except Exception as e:
        return f"Error: {str(e)}"