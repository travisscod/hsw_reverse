import random
import time
from typing import List, Dict
import json

def pdc(st):
    return json.dumps({
        "S": int(st * 1000),  # Convert the provided time to milliseconds
        "N": 0,
        "P": 0,
        "Gcs": random.choice(range(40,110))  # Generate a random number between 40 and 110
    })
    
def pem(): 
    return {'csc': random.randint(110, 140) }


