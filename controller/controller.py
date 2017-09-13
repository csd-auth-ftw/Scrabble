import pygame

from controller.events import TickEvent, QuitEvent


class Controller(object):
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register(QuitEvent, self)
        #self.play_sound()

        self.running = True

    def Run(self):
        while self.running:
            self.event_manager.post(TickEvent())

    def on_quit(self, event):
        self.running = False

    def play_sound(self):
        pygame.mixer.music.load('sounds\main.mp3')
        pygame.mixer.music.play(-1)
