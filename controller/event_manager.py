from weakref import WeakKeyDictionary


class EventManager:
    def __init__(self):
        self.listeners = WeakKeyDictionary()

    def register(self, event, listener):
        if event not in self.listeners:
            self.listeners[event] = []

        self.listeners[event].append(listener)

    def remove(self, event, listener = None):
        if event not in self.listeners:
            return

        # delete all listeners for an event
        if listener == None:
            del self.listeners[event]
            return

        # delete a specific listener
        self.listeners[event].remove(listener)

    def post(self, event):
        if event.__class__ not in self.listeners:
            return

        # copy listeners to avoid size change during loop
        listeners = self.listeners[event.__class__][:]
        for listener in listeners:
            event.apply(listener)
