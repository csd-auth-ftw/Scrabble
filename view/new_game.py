import pygame

from controller.events import ClickEvent, TileRemovedEvent
from model.bag import Bag
from model.player import Player, CPU_MODE_SMART
from utilities import config
from view.board import Board
from view.button import Button
from view.deck import Deck
from view.score_board import ScoreBoard
from view.view import View
import os


class NewGame(View):
    def __init__(self, event_manager):
        super().__init__(event_manager)

        self.clock = pygame.time.Clock()
        self.std_font = pygame.font.SysFont("sans-serif", 22)
        self.button_font = pygame.font.SysFont("monospace", 24)
        self.board = Board(self.event_manager, 50, 100, 1, 7)

        self.options = [Button(self.button_font, config.END_ROUND, (235, 150), self.on_end_round_click),
                        Button(self.button_font, config.CLEAR, (150, 200), self.on_clear_click),
                        Button(self.button_font, config.BACKSPACE, (350, 200), self.on_backspace_click)
                        ]

        # init players
        self.player_a = Player('Player 1')
        self.player_b = Player('PC')
        self.render_sleep = 0

        # todo remove
        self.player_a.is_playing = True

        self.score_board = ScoreBoard(self.player_a, self.player_b, 20, 20)
        self.deck = Deck(self.event_manager, 50, 350)
        self.bag = Bag()
        self.set_deck()

        for option in self.options:
            self.event_manager.register(ClickEvent, option)

    def on_clear_click(self, button, event):
        self.board.on_press_esc(event)

    def on_end_round_click(self, button, event):
        self.play()

    def on_backspace_click(self, button, event):
        self.board.on_press_backspace(event)

    def set_deck(self):
        if (self.bag.remaining_chars() < config.MAX_WORD_LEN):
            return False

        for i in range(config.MAX_WORD_LEN):
            self.deck.append_character(self.bag.get_char())

        return True

    def flip_players(self):
        self.player_a.is_playing = not self.player_a.is_playing
        self.player_b.is_playing = not self.player_b.is_playing

    def play(self):
        word, word_score = self.board.get_word()

        # check user word and update score
        if word in config.GREEK7_WORDS:
            self.player_a.add_score(word_score)
            self.player_a.append_word(word)

        # clear deck and board
        unused_chars = self.deck.clear()
        self.bag.append_chars(unused_chars)
        self.board.clear()

        # computer turn
        self.flip_players()

        if (self.bag.remaining_chars() < config.MAX_WORD_LEN):
            # TODO end game
            print("END_GAME")
            pass

        deck_cpu = []
        for i in range(config.MAX_WORD_LEN):
            deck_cpu.append(self.bag.get_char()[0])

        # TODO add back to bag deck_cpu not used chars
        word_cpu = self.player_a.cpu_play(deck_cpu, CPU_MODE_SMART)

        if word_cpu is None:
            # TODO alert user
            pass
        else:
            self.player_b.append_word(word_cpu[0])
            self.player_b.add_score(word_cpu[1])
            self.board.set_word(word_cpu[0])

        self.render_sleep = 1

    def render(self):
        # draw background
        self.render_background()

        # draws the score board
        self.score_board.render()

        # draws the board
        self.board.render()

        # draws the options
        for option in self.options:
            option.render(self.screen)

        # draws the decks
        self.deck.render()

        # draws the number of remaining chars
        self.render_remaining_chars()

        # limit to 60 frames per second
        self.clock.tick(60)

        # go ahead and update the screen with what we've drawn
        pygame.display.flip()

        # checks if CPU is playing
        self.check_sleep()


    def on_destroy(self):
        print("destroy new_game view")

        # call nested views on_destroy
        self.score_board.on_destroy()
        self.board.on_destroy()
        self.deck.on_destroy()

        for option in self.options:
            self.event_manager.remove(ClickEvent, option)

    def check_sleep(self):
        if self.render_sleep > 0:
            self.render_sleep += 1

            if self.render_sleep > 3:
                pygame.time.delay(5000)
                self.render_sleep = 0
                self.board.clear()
                self.flip_players()

                # TODO
                if not self.set_deck():
                    print("TODO END GAME")

    def render_remaining_chars(self):
        rem_chars_render = self.std_font.render("remaining: " + str(self.bag.remaining_chars()), 1, (255, 255, 255))
        self.screen.blit(rem_chars_render, (config.SCREEN_W - 140, config.SCREEN_H - 100))

    def render_background(self):
        img_path = os.path.normpath(os.path.dirname(__file__) + "/../res/images/green_fabric.jpg")
        img = pygame.image.load(img_path)
        self.screen.fill(config.BLACK)
        for x in range(0, config.SCREEN_W, img.get_rect().width):
            for y in range(0, config.SCREEN_H, img.get_rect().height):
                self.screen.blit(img, (x, y))
