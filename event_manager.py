import pygame


class EventManager:
    def __init__(self):
        self.general_events = {}
        self.key_events = {}

    def on(self, type, handler):
        self.add_event_handler(self.general_events, type, handler)

    def on_key_down(self, key, handler):
        self.add_event_handler(self.key_events, key, handler)

    def add_event_handler(self, list, key, handler):
        if key not in list:
            list[key] = []
        else:
            if handler in list[key]:
                return

        list[key].append(handler)

    def off(self, type, handler):
        self.remove_event_handler(self.general_events, type, handler)

    def off_key_down(self, key, handler):
        self.remove_event_handler(self.key_events, key, handler)

    def remove_event_handler(self, list, key, handler):
        if key in list:
            if handler in list[key]:
                list[key].remove(handler)

    def check(self):
        for event in pygame.event.get():
            # check quit event
            if event.type == pygame.QUIT:
                return True

            if event.type in self.general_events:
                for handler in self.general_events[event.type]:
                    handler(event)

            if event.type == pygame.KEYDOWN and event.key in self.key_events:
                for handler in self.key_events[event.key]:
                    handler(event)

        return False
