import pygame
import sys
import config
from bag import Bag
from controller import Controller


def main():
    pygame.init()
    pygame.display.set_mode((config.SCREEN_W, config.SCREEN_H))
    pygame.display.set_caption("Scrabble")
    controller = Controller()
    #controller.game_intro()
    controller.start_screen()
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
