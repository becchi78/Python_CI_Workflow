"""
Lambda function to process events from various sources.
"""
from typing import Any, Dict
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def validate_event(event: Dict[str, Any]) -> bool:
    """
    Validates the incoming event data.
    
    Args:
        event: The event data to validate
        
    Returns:
        bool: True if the event is valid, False otherwise
    """
    required_fields = ['userId', 'eventType', 'timestamp']
    return all(field in event for field in required_fields)

def process_event(event: Dict[str, Any]) -> Dict[str, Any]:
    """
    Processes the event data and performs necessary transformations.
    
    Args:
        event: The event data to process
        
    Returns:
        Dict containing the processed event data
    """
    if not validate_event(event):
        raise ValueError("Invalid event format")
    
    processed_event = {
        'user_id': event['userId'],
        'event_type': event['eventType'],
        'timestamp': event['timestamp'],
        'processed_at': event.get('processedAt', ''),
        'metadata': event.get('metadata', {})
    }
    
    return processed_event

def lambda_handler(event: Dict[str, Any], context: Any) -> Dict[str, Any]:
    """
    AWS Lambda handler function.
    
    Args:
        event: The AWS Lambda event
        context: The AWS Lambda context
        
    Returns:
        Dict containing the response
    """
    try:
        logger.info("Received event: %s", json.dumps(event))
        
        processed_result = process_event(event)
        
        return {
            'statusCode': 200,
            'body': json.dumps(processed_result)
        }
        
    except ValueError as e:
        logger.error("Validation error: %s", str(e))
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
        
    except Exception as e:
        logger.error("Unexpected error: %s", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal server error'})
        }
