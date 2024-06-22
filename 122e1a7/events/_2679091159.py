import json
import ncrypt

#Intl.DateTimeFormat().resolvedOptions().timeZone

class Event:
    def __init__(self, timezone):
        self.hash = json.dumps(timezone)