import pygame

from utilities import config
from view import tile
from view.tile import Tile
from view.view import View
from controller.events import PressEvent, TilePickedEvent, TileRemovedEvent


class Board(View):
    def __init__(self, event_manager, pos_x, pos_y, rows, cols):
        super().__init__(event_manager)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rows = rows
        self.cols = cols
        self.tile_width = config.BOARD_TILE_WIDTH
        self.tile_height = config.BOARD_TILE_HEIGHT
        self.tiles = []  # NxN for future usage

        self.event_manager.register(PressEvent, self)
        self.event_manager.register(TilePickedEvent, self)

        self.init_tiles()

    # init with empty tiles
    def init_tiles(self):
        for x in range(self.rows):
            self.tiles.append([])
            for y in range(self.cols):
                self.tiles[x].append(None)

    # get first empty column index
    def get_empty_col(self, row):
        for c in range(self.cols):
            if self.tiles[row][c] == None:
                return c

        return -1

    # get the last tile (and its position) of a row
    def get_last_tile(self, row):
        for c in reversed(range(self.cols)):
            tile = self.tiles[row][c]

            if tile == None:
                continue

            return (tile, c)

        return (None, -1)

    # called when a tile from the deck is picked
    def on_tile_picked(self, event):
        # insert to the first row
        col = self.get_empty_col(0)
        self.tiles[0][col] = event.tile

        # set new tile position
        pos_x = self.pos_x + (config.MARGIN + self.tile_width) * col + config.MARGIN
        pos_y = self.pos_y + config.MARGIN
        event.tile.move(pos_x, pos_y, self.tile_width, self.tile_height)

    def on_press_backspace(self, event):
        tile = self.get_last_tile(0)

        # ignore if there are no tiles
        if tile[1] == -1:
            return

        # remove tile from board
        self.tiles[0][tile[1]] = None

        # move tile to deck
        self.event_manager.post(TileRemovedEvent(tile[0]))

    # clear board on esc
    def on_press_esc(self, event):
        for c in range(self.cols):
            if self.tiles[0][c] == None:
                continue

            # move tile to deck
            self.event_manager.post(TileRemovedEvent(self.tiles[0][c]))

            self.tiles[0][c] = None

    def render(self):
        # render background
        for r in range(self.rows):
            for c in range(self.cols):
                pos_x = self.pos_x + (config.MARGIN + self.tile_width) * c + config.MARGIN
                pos_y = self.pos_y + (config.MARGIN + self.tile_height) * r + config.MARGIN
                pygame.draw.rect(self.screen, (0, 0, 255), [pos_x, pos_y, self.tile_width, self.tile_height])

        # render tiles
        for x in range(self.rows):
            for y in range(self.cols):
                if not self.tiles[x][y] == None:
                    self.tiles[x][y].render()

    def clear(self):
        for x in range(self.rows):
            for y in range(self.cols):
                self.tiles[x][y] = None

    def set_word(self, word):
        for i in range(len(word)):
            pos_x = self.pos_x + (config.MARGIN + self.tile_width) * i + config.MARGIN
            pos_y = self.pos_y + config.MARGIN

            self.tiles[0][i] = Tile(pos_x, pos_y, self.tile_width, self.tile_height, word[i], config.GREEK_CHAR_DICT[word[i]]['points'])


    def get_word(self):
        word = ''
        score = 0
        for x in range(self.rows):
            for y in range(self.cols):
                if not self.tiles[x][y] == None:
                    word += self.tiles[x][y].char
                    score += self.tiles[x][y].char_value

        return (word, score)

    def on_destroy(self):
        self.event_manager.remove(PressEvent, self)
        self.event_manager.remove(TilePickedEvent, self)

    def get_tiles(self):
        return self.tiles

    def get_tile(self, x, y):
        return self.tiles[x][y]
