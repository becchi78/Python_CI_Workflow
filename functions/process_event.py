"""Process event module."""
from typing import Dict, Any

def add_numbers(a: int,b: int) -> int:  # E231: missing whitespace after comma
    return a+b  # E226: missing whitespace around operator

def process_data(data: Dict[str, Any]):  # no-untyped-def: missing return type
    """Process input data."""
    if data["value"] > 0:
        return data["value"]   # E201: whitespace after '{'
    return 0
