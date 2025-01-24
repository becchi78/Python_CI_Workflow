from typing import Dict, Any

def add_numbers(a: int,b: int) -> int:  # flake8: E231 - missing whitespace after comma
    x=1  # flake8: E225 - missing whitespace around operator
    return a+b  # flake8: E226 - missing whitespace around arithmetic operator

def process_data(data: Dict[str, Any]):  # mypy: missing return type annotation
    if data["value"] > 0:
        return "positive"
    else:
        return "negative"

def unreachable_function():  # pytest-cov: function never called
    return "this function is never used"
