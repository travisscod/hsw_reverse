import ncrypt 
import json


# Webgl Renderer and Vendor encrypted

class Event:
    def __init__(self, renderer, vendor) -> None:
        self.hash = json.dumps(
            json.dumps(
                [
                    ncrypt.encrypt(vendor), 
                    ncrypt.encrypt(renderer)
                ]
            )
        )
                                   
        

