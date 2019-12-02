import pygame


class Pacman:

    GAME_WIDTH = 224
    GAME_HEIGHT = 288

    def __init__(self):
        pygame.init()
        win = pygame.display.set_mode((self.GAME_WIDTH, self.GAME_HEIGHT))
        pygame.display.set_caption("Pacman")

        run = True
        while run:
            pygame.time.delay(10)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            win.fill((0, 0, 0))
            pygame.draw.rect(
                win,
                (255, 255, 255),
                (3, 3, self.GAME_WIDTH - 6, self.GAME_HEIGHT - 6))
            pygame.display.update()

        pygame.quit()
    

    @staticmethod
    def start():
        Pacman()



if __name__ == "__main__":
    Pacman.start()
