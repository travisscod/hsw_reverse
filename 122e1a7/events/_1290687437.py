import time
import random

#this is some sort of performance now but idk if it correlates to other things also.

class Event:
    def __init__(self) -> None:
        self.hash = random.randint(300, 450)#time.time() - time.time()