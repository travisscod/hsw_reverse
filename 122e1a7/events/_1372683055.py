import datetime

class Event:
    def __init__(self) -> None:
        self.hash = f"[{str(datetime.now().hour)}]"
    