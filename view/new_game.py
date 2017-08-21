import pygame

from model import bag
from model import board
from model import player
from utils import config
from view.view import View


class NewGame(View):
    def __init__(self, event_manager):
        self.screen = pygame.display.get_surface()
        self.screen = pygame.display.set_mode(config.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.event_manager = event_manager
        self.font = pygame.font.Font(None, 24)
        self.board = board.Board(self.screen, 15, 15)
        # self.deckA = deck.Deck(self.screen, 100, 730)
        self.playerA = player.Player('new player', self.screen, 100, 730)
        self.bag = bag.Bag()

        self.board.init_grid()
        self.bag.init_bag()
        self.playerA.init_deck(self.bag)

    def render(self):
        self.screen.fill(config.BLACK)
        # draws the board
        self.board.render()
        # draws the decks
        self.playerA.render()

        # Limit to 60 frames per second
        self.clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def on_destroy(self):
        print("destroy new_game view")
        