"""
Test cases for the process_event Lambda function.
"""
import pytest
from functions.process_event import validate_event, process_event, lambda_handler

def test_validate_event_valid():
    """Test event validation with valid data."""
    event = {
        'userId': '12345',
        'eventType': 'click',
        'timestamp': '2024-01-21T10:00:00Z'
    }
    assert validate_event(event) is True

def test_validate_event_invalid():
    """Test event validation with invalid data."""
    event = {
        'userId': '12345',
        'timestamp': '2024-01-21T10:00:00Z'
    }
    assert validate_event(event) is False

def test_process_event_success():
    """Test successful event processing."""
    event = {
        'userId': '12345',
        'eventType': 'click',
        'timestamp': '2024-01-21T10:00:00Z',
        'metadata': {'page': 'home'}
    }
    
    result = process_event(event)
    
    assert result['user_id'] == '12345'
    assert result['event_type'] == 'click'
    assert result['timestamp'] == '2024-01-21T10:00:00Z'
    assert result['metadata'] == {'page': 'home'}

def test_process_event_invalid():
    """Test event processing with invalid data."""
    event = {
        'userId': '12345',
        'timestamp': '2024-01-21T10:00:00Z'
    }
    
    with pytest.raises(ValueError):
        process_event(event)

def test_lambda_handler_success():
    """Test successful Lambda handler execution."""
    event = {
        'userId': '12345',
        'eventType': 'click',
        'timestamp': '2024-01-21T10:00:00Z'
    }
    
    result = lambda_handler(event, None)
    
    assert result['statusCode'] == 200
    assert 'body' in result

def test_lambda_handler_invalid_event():
    """Test Lambda handler with invalid event."""
    event = {
        'userId': '12345',
        'timestamp': '2024-01-21T10:00:00Z'
    }
    
    result = lambda_handler(event, None)
    
    assert result['statusCode'] == 400
    assert 'error' in result['body']
