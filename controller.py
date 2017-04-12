import pygame

import bag
import board
import button
import deck
import config
import event_manager
import sys

import player


class Controller(object):
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pygame.time.Clock()
        self.event_manager = event_manager.EventManager()
        self.font = pygame.font.Font(None, 24)
        self.board = board.Board(self.screen, 15, 15)
        # self.deckA = deck.Deck(self.screen, 100, 730)
        self.playerA = player.Player('new player', self.screen, 100, 730)
        self.bag = bag.Bag()

        # set event handlers
        self.event_manager.on(pygame.MOUSEBUTTONDOWN, self.on_click_handler)
        self.event_manager.on_key_down(pygame.K_SPACE, self.on_press_space)

    def game_intro(self):

        done = False
        screen = pygame.display.set_mode(config.WINDOW_SIZE)
        menu_font = pygame.font.Font(None, 40)
        options = [button.Button(screen, menu_font, "NEW GAME", (140, 105)),
                   button.Button(screen, menu_font, "LOAD GAME", (135, 155)),
                   button.Button(screen, menu_font, "OPTIONS", (145, 205))]

        while not done:
            done = self.event_manager.check()
            screen.fill(config.WHITE)

            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()

            pygame.display.update()
            self.clock.tick(60)

    def start_screen(self):
        self.board.init_grid()
        self.bag.init_bag()
        self.playerA.init_deck(self.bag)
        self.play_sound(0)

        screen = pygame.display.set_mode(config.WINDOW_SIZE)

        done = False
        display_start_screen = True

        while not done and display_start_screen:
            done = self.event_manager.check()

            # clears the screen
            screen.fill(config.BLACK)

            # draws the board
            self.board.render()

            # draws the decks
            self.playerA.render()

            # Limit to 60 frames per second
            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

    def on_click_handler(self, event):

        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (config.WIDTH + config.MARGIN)
        row = pos[1] // (config.HEIGHT + config.MARGIN)

        print("Click ", pos, "Grid coordinates: ", row, column)

    def on_press_space(self, event):
        self.play_sound(1)
        self.playerA.pick_letter(self.bag)

    def play_sound(self, type):
        sounds = {
            0: 'sounds\main.mp3',
            1: 'sounds\sound_effect.mp3'
        }

        if type == 0:
            pygame.mixer.music.load(sounds.get(type))
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.load(sounds.get(type))
            pygame.mixer.music.play(1)

    def quit_game(self):
        pygame.quit()
        sys.exit()
