"""Test process event module."""
import pytest
from functions.process_event import add_numbers, process_data

def test_add_numbers():
    """Test add_numbers function."""
    assert add_numbers(1, 2) == 4  # Will fail: 1 + 2 should be 3

def test_process_data_positive():
    """Test process_data with positive value."""
    data = {"value": 5}
    assert process_data(data) == 5

# test_process_data_negative is missing, affecting coverage
