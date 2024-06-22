import json

#webgl renderer and vendor

class Event:
    def __init__(self, vendor, renderer):
        self.hash = json.dump([vendor, renderer])