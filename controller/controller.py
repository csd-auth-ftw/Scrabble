from controller.events import TickEvent, QuitEvent


class Controller(object):
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.event_manager.register(QuitEvent, self)

        self.running = True

    def Run(self):
        while self.running:
            self.event_manager.post(TickEvent())

    def on_quit(self, event):
        self.running = False

    #
    # def on_click_handler(self, event):
    #
    #     # User clicks the mouse. Get the position
    #     pos = pygame.mouse.get_pos()
    #     # Change the x/y screen coordinates to grid coordinates
    #     column = pos[0] // (config.WIDTH + config.MARGIN)
    #     row = pos[1] // (config.HEIGHT + config.MARGIN)
    #
    #     print("Click ", pos, "Grid coordinates: ", row, column)
    #
    # def on_press_space(self, event):
    #     self.play_sound(1)
    #     self.playerA.pick_letter(self.bag)
    #
    # def play_sound(self, type):
    #     sounds = {
    #         0: 'sounds\main.mp3',
    #         1: 'sounds\sound_effect.mp3'
    #     }
    #
    #     if type == 0:
    #         pygame.mixer.music.load(sounds.get(type))
    #         pygame.mixer.music.play(-1)
    #     else:
    #         pygame.mixer.music.load(sounds.get(type))
    #         pygame.mixer.music.play(1)
    #
    # def quit_game(self):
    #     pygame.quit()
    #     sys.exit()
