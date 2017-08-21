import pygame

from controller.events import TickEvent, QuitEvent, NewGameEvent, LoadGameEvent, OptionsEvent
from utils import config


class PyGameController:

    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.RegisterListener(self)

    def handleButtonClick(self):
        pos = pygame.mouse.get_pos()
        button_text = self.event_manager.getButtonText(pos)
        if button_text == config.NEW_GAME:
            print("New game")
            return NewGameEvent()
        elif button_text == config.LOAD_GAME:
            print("Load game")
            return LoadGameEvent()
        elif button_text == config.OPTIONS:
            print("Options")
            return OptionsEvent()

    def Notify(self, event):
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                ev = None
                if event.type == pygame.QUIT:
                    ev = QuitEvent()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # TODO check if it is a button or not
                    ev = self.handleButtonClick()

                if ev:
                    self.event_manager.Post(ev)

