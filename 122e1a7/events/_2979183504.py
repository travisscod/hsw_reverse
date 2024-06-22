import json
import ncrypt


class Event:
    def __init__(self, Q) -> None:
        self.hash = json.dumps(ncrypt.encrypt(Q))