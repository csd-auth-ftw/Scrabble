import pygame

from utilities import config
from view import tile
from view.view import View
from controller.events import PressEvent, TilePickedEvent, TileRemovedEvent


class Board(View):
    def __init__(self, event_manager, pos_x, pos_y, rows=1, cols=20):
        super().__init__(event_manager)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rows = rows
        self.cols = cols
        self.tiles = [] # NxN for future usage

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
        pos_x = self.pos_x + (config.MARGIN + config.WIDTH) * col + config.MARGIN
        pos_y = self.pos_y + config.MARGIN
        event.tile.move(pos_x, pos_y)

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
                pos_x = self.pos_x + (config.MARGIN + config.WIDTH) * c + config.MARGIN
                pos_y = self.pos_y + (config.MARGIN + config.HEIGHT) * r + config.MARGIN
                pygame.draw.rect(self.screen, (0, 0, 255), [pos_x, pos_y, config.WIDTH, config.HEIGHT])

        # render tiles
        for x in range(self.rows):
            for y in range(self.cols):
                if not self.tiles[x][y] == None:
                    self.tiles[x][y].render()

    def get_tiles(self):
        return self.tiles

    def get_tile(self, x, y):
        return self.tiles[x][y]
