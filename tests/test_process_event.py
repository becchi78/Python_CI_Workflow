"""Test process event module."""
import pytest
from functions.process_event import add_numbers, process_data

def test_add_numbers():
    """Test add_numbers function."""
    assert add_numbers(1, 2) == 4  # Will fail: 1 + 2 should be 3

def test_process_data_active():
    """Test process_data with active status."""
    data = {"status": "active"}
    assert process_data(data) is True

# test_process_data_inactive が未実装なので、カバレッジが下がります
