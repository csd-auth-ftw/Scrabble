import pygame

from controller.events import TickEvent, QuitEvent, ClickEvent, PressEvent
from utilities import config


class PyGameController:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register(TickEvent, self)

    def on_tick(self, event):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.event_manager.post(QuitEvent())
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.event_manager.post(ClickEvent())
            if event.type == pygame.KEYDOWN:
                self.event_manager.post(PressEvent(event.key))
