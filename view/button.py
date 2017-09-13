from utilities import config
import pygame

from view.view import View


class Button(View):
    hovered = False

    def __init__(self, font = None, text = '', pos = None, click_listener = None):
        super().__init__()
        self._text = text
        self.pos = pos

        if font is None:
            self._font = pygame.font.SysFont("monospace", 24)
        else:
            self._font = font

        self.click_listener = click_listener
        self.set_rect()

    def on_click(self, event):
        if callable(self.click_listener):
            self.click_listener(self, event)

    def render(self, screen):
        self.set_rend()
        self.set_hovered()
        screen.blit(self.rend, self.rect)

    def set_hovered(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.hovered = True
        else:
            self.hovered = False

    def set_rend(self):
        self.rend = self._font.render(self._text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return config.GREEN
        else:
            return config.RED

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def get_rect(self):
        return self.rect

    def get_text(self):
        return self._text
