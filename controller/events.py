class Event:
    def __init__(self):
        self.name = "event";

    def __str__(self) -> str:
        return super().__str__()


class TickEvent(Event):
    def __init__(self):
        self.name = "CPU tick"


class QuitEvent(Event):
    def __init__(self):
        self.name = "Quit"


class NewGameEvent(Event):
    def __init__(self):
        self.name = "New game"


class LoadGameEvent(Event):
    def __init__(self):
        self.name = "Load game"


class OptionsEvent(Event):
    def __init__(self):
        self.name = "Options"