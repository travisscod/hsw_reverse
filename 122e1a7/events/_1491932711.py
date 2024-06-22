import json
import ncrypt


# DONT KNOW YET BUT INDEX 1 is encrypted to 2979183504 and in that case its 306544771890

class Event:
    def __init__(self, jsHeapSizeLimit, ServiceWorkerContainer,
                 PushManager, indexedDB, connection_type) -> None:
        data = [
            2147483648,  #random idk
            306544771890, #random idk THIS GETS USED IN 
            "null",  #random idk yet
            "null",  #random idk yet
            jsHeapSizeLimit,#4294705152, #performance.memory.jsHeapSizeLimit 
            ServiceWorkerContainer,#"true",  #'ServiceWorkerContainer' in window
            PushManager,# "true",  #"PushManager"in window
            indexedDB, #"true",  #"indexedDB"in window 
            connection_type, #"null" #navigator.connection.type or null but is always null for some reason
        ]
        self.hash = json.dumps("".join(str(data)).replace(" ", ""))