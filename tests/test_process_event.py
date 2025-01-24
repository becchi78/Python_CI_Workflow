from functions.process_event import add_numbers, process_data

def test_add_numbers():
    assert add_numbers(1, 2) == 4  # This will fail in pytest

def test_process_data():
    data = {"value": 5}
    assert process_data(data) == "positive"

# Note: unreachable_function is not tested, which will affect coverage
