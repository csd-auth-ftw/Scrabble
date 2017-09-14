import pygame

from utilities import config
from view import tile
from view.tile import Tile
from view.view import View
from controller.events import ClickEvent, TilePickedEvent, TileRemovedEvent


class Deck(View):
    def __init__(self, event_manager, pos_x, pos_y, tiles_number=7):
        super().__init__(event_manager)

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tiles_number = tiles_number
        self.tiles = []

        self.tile_width = config.DECK_TILE_WIDTH
        self.tile_height = config.DECK_TILE_HEIGHT

        self.event_manager.register(ClickEvent, self.on_tile_click)
        self.event_manager.register(TileRemovedEvent, self)

        self.init_deck()

    def init_deck(self):
        for i in range(self.tiles_number):
            self.tiles.append(None)

    def on_tile_click(self, event):
        # check if hit any tile
        for i in range(self.tiles_number):
            tile = self.tiles[i]

            if tile == None:
                continue

            if tile.get_rect().collidepoint(event.pos):
                # remove tile from deck
                self.tiles[i] = None

                self.event_manager.post(TilePickedEvent(tile))

    def on_tile_removed(self, event):
        pos = self.get_free_tile()

        # insert to tiles list
        self.tiles[pos] = event.tile

        pos_x = self.pos_x + (config.MARGIN + self.tile_width) * pos + config.MARGIN
        pos_y = self.pos_y + config.MARGIN
        event.tile.move(pos_x, pos_y, self.tile_width, self.tile_height)

    # returns the first free tile position
    def get_free_tile(self):
        for i in range(self.tiles_number):
            if self.tiles[i] == None:
                return i

        return -1

    def clear(self):
        char = []
        for i in range(self.tiles_number):
            if not self.tiles[i] is None:
                char.append((self.tiles[i].char,self.tiles[i].char_value))
                self.tiles[i] = None

        return char

    def append_character(self, character):
        pos = self.get_free_tile()

        if pos == -1:
            return False
        pos_x = self.pos_x + (config.MARGIN + self.tile_width) * pos + config.MARGIN
        pos_y = self.pos_y + config.MARGIN

        self.tiles[pos] = Tile(pos_x, pos_y, self.tile_width, self.tile_height, character[0], character[1])
        return True

    def render(self):
        # render background
        for i in range(self.tiles_number):
            left = self.pos_x + (config.MARGIN + self.tile_width) * i + config.MARGIN
            top = self.pos_y + config.MARGIN
            pygame.draw.rect(self.screen, (0, 255, 0), [left, top, self.tile_width, self.tile_height])

        # render tiles
        for tile in self.tiles:
            if tile is not None:
                tile.render()
        pass

    def on_destroy(self):
        self.event_manager.remove(ClickEvent, self.on_tile_click)
        self.event_manager.remove(TileRemovedEvent, self)
