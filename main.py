from controller.controller import Controller
from controller.event_manager import EventManager
from controller.pygame_controller import PyGameController
from view.pygame_view import PygameView
from utilities import utils


def main():
    em = EventManager()

    utils.generate_greek7()

    pygame_view = PygameView(em)
    pygame_controller = PyGameController(em)
    controller = Controller(em)

    controller.Run()

if __name__ == '__main__':
    main()
