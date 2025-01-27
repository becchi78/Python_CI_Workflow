"""Process event module."""
from typing import Dict, Any

def add_numbers(a : int,b:int)-> int: # E203, E231
    return a +b  # E225

def process_data(data):  # 型アノテーション抜き
    if data['status'] == 'active':
        return True
    return False
