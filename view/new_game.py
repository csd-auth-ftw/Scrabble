import pygame

from controller.events import PressEvent, ClickEvent
from model import bag
from model import player
from model.button import Button
from utilities import config
from view import board, deck
from view.score_board import ScoreBoard
from view.view import View


class NewGame(View):
    def __init__(self, event_manager):
        self.screen = pygame.display.get_surface()
        self.screen = pygame.display.set_mode(config.WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.event_manager = event_manager
        self.button_font = pygame.font.SysFont("monospace", 24)
        self.board = board.Board(self.screen, 1, 7)

        self.options = [Button(self.button_font, config.PICK_LETTER, (635, 105), self.on_pick_letter_click),
                        Button(self.button_font, config.END_ROUND, (635, 155), self.on_end_round_click),
                        ]

        # self.deckA = deck.Deck(self.screen, 100, 730)
        self.playerA = player.Player('new player')
        self.score_board = ScoreBoard(self.playerA, self.playerA, 20, 20)
        self.deck = deck.Deck(self.screen, 50, 350)
        self.bag = bag.Bag()

        self.event_manager.register(PressEvent, self)
        for option in self.options:
            self.event_manager.register(ClickEvent, option)


    def on_pick_letter_click(self, button, event):
        self.playerA.pick_letter(self.bag)

    def on_end_round_click(self, button, event):
        print("end round")

    def on_press(self, event):
        print("i pressed key with code:" + str(event.keyCode))

    def on_press_space(self, event):
        self.playerA.pick_letter(self.bag)

    def on_press_enter(self, event):
        print("i pressed enter")

    def render(self):
        self.screen.fill(config.BLACK)

        # draws the score board
        self.score_board.render()

        # draws the board
        self.board.render()

        # draws the decks
        self.deck.render()

        # Limit to 60 frames per second
        self.clock.tick(60)

        for option in self.options:
            option.render(self.screen)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def on_destroy(self):
        print("destroy new_game view")
        for option in self.options:
            self.event_manager.remove(ClickEvent, option)
        