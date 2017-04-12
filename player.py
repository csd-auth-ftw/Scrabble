import deck


class Player:
    def __init__(self, name, screen, deck_pos_x, deck_pos_y):
        self.name = name
        self.score = 0
        self.deck = deck.Deck(screen, deck_pos_x, deck_pos_y)

    def render(self):
        self.deck.render()

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def pick_letter(self, bag):
        pos = self.deck.get_free_tile()

        if pos > -1:
            letter, letter_value = bag.get_letter()
            self.deck.tiles[pos].put_letter(letter, letter_value, 1)
        else:
            print("Not enough space")

    def init_deck(self, bag):
        self.deck.init_deck()

        # if not self.deck.tiles:
        #     return
        #
        # for i in range(self.deck.tiles_number):
        #     deck_tile = self.deck.tiles[i]
        #     letter, letter_value = bag.get_letter()
        #
        #     if deck_tile.is_empty():
        #         deck_tile.put_letter(letter, letter_value, 1)
        #     else:
        #         deck_tile.empty()
