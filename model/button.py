from utils import config


class Button:
    hovered = False

    def __init__(self, menu_font, text, pos):
        self.text = text
        self.pos = pos
        self.menu_font = menu_font
        self.set_rect()

    def draw(self, screen):
        self.set_rend()
        screen.blit(self.rend, self.rect)

    def set_rend(self):
        self.rend = self.menu_font.render(self.text, True, self.get_color())

    def get_color(self):
        if self.hovered:
            return config.GREEN
        else:
            return config.BLACK

    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

    def get_rect(self):
        return self.rect

    def get_text(self):
        return self.text
