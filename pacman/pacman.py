import pygame
from helper_code import scale


class Pacman:

    GAME_WIDTH = 224
    GAME_HEIGHT = 288

    def __init__(self):
        """ This is the top-level code for pacman. We initialise 
        pygame and then stay in the loop until the red cross on the window
        is clicked.
        """
        # window_size = pygame.display.get_window_size()
        # self.WINDOW_WIDTH = win
        pygame.init()
        win = pygame.display.set_mode(
            (self.GAME_WIDTH, self.GAME_HEIGHT), pygame.RESIZABLE)
        pygame.display.set_caption("Pacman")

        game_surface = pygame.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))

        run = True
        while run:
            pygame.time.delay(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.VIDEORESIZE:
                    win = pygame.display.set_mode(
                        (event.w, event.h), pygame.RESIZABLE)
                    self.window_width = event.w
                    self.window_height = event.h

            pygame.draw.rect(
                game_surface,
                (255, 255, 255),
                (10, 10, self.GAME_WIDTH - 20, self.GAME_HEIGHT - 20))

            scale(
                win,
                game_surface,
                (self.GAME_WIDTH, self.GAME_HEIGHT),
                (self.window_width, self.window_height))

            pygame.display.update()

        pygame.quit()
