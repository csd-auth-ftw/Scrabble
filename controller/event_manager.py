from weakref import WeakKeyDictionary


class EventManager:
    def __init__(self):
        self.listeners = WeakKeyDictionary()
        self.button_listeners = {}

    def RegisterButtonListener(self, button, listener):
        self.button_listeners[button] = listener

    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    def UnregisterButtonListener(self, button):
        if button in self.button_listeners.keys():
            del self.button_listeners[button]

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def PostButton(self, event):
        for button_listener in self.button_listeners.keys():
            button_listener.OnClick(event)

    def Post(self, event):
        for listener in self.listeners.keys():
            listener.Notify(event)

    def getButtonText(self, mouse_position):
        for button in self.button_listeners:
            if button.get_rect().collidepoint(mouse_position):
                return button.get_text()
