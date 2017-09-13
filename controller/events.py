import pygame

class Event:
    def __init__(self, name, method_name):
        self.name = name
        self.method_name = method_name

    def apply(self, listener):
        # if its a function or method call it
        if callable(listener):
            listener(self)
        # else if its an object, call the method
        elif True: # TODO fix, check if listener is object
            method = getattr(listener, self.method_name, None)
            if callable(method):
                method(self)

class TickEvent(Event):
    def __init__(self):
        super().__init__("TickEvent", "on_tick")

class LeaderBoardEvent(Event):
    def __init__(self):
        super().__init__("LeadBoardEvent","on_leader_board")

class QuitEvent(Event):
    def __init__(self):
        super().__init__("QuitEvent", "on_quit")

class NewGameEvent(Event):
    def __init__(self):
        super().__init__("NewGameEvent", "on_new_game")

class ClickEvent(Event):
    def __init__(self, pos = None):
        super().__init__("ClickEvent", "on_click")
        self.get_rect_name = "get_rect"
        if pos == None:
            self.pos = pygame.mouse.get_pos()
        else:
            self.pos = pos

    def apply(self, listener):
        # if its a function call it
        if callable(listener):
            listener(self)
        elif True: # TODO fix, check if listener is object
            # check for get_rect to call only if
            # there's a collision
            get_rect = getattr(listener, self.get_rect_name, None)
            method = getattr(listener, self.method_name, None)

            if callable(method):
                if (callable(get_rect)):
                    if get_rect().collidepoint(self.pos):
                        method(self)
                else:
                    method(self)

class PressEvent(Event):
    def __init__(self, keyCode):
        super().__init__("PressEvent", "on_press")
        self.keyCode = keyCode
        self.keyCodeNames = {
            32: "space",
            13: "enter"
        }

    def apply(self, listener):
        # if its a function call it
        if callable(listener):
            listener(self)
        elif True: # TODO fix, check if listener is object
            # check for specific key method
            if self.keyCode in self.keyCodeNames:
                key_method_name = self.method_name + "_" + self.keyCodeNames[self.keyCode]
                key_method = getattr(listener, key_method_name, None)
                if callable(key_method):
                    key_method(self)
                    return

            # check for default method
            method = getattr(listener, self.method_name, None)
            if callable(method):
                method(self)