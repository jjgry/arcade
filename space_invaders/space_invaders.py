import pygame
from space_invaders.enemy import Enemy
from space_invaders.player import Player
from space_invaders.projectile import Projectile
from space_invaders.block import Block
from space_invaders.wave import Wave


class SpaceInvaders:

    WINDOW_WIDTH = 500
    WINDOW_HEIGHT = 500

    def __init__(self):
        """ This is the top-level code for space invaders. We initialise 
        pygame and then stay in the loop until the red cross on the window
        is clicked.
        """
        pygame.init()
        win = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Space Invaders")

        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 20)

        wave = Wave(self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

        run = True
        while run:
            pygame.time.delay(10)  # pause for some number of ms

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            keys = pygame.key.get_pressed()

            # update everything
            wave.update(keys)

            # draw everything
            win.fill((0, 0, 0))
            if wave.player.lives > 0:
                wave.draw(win)
                lives_text = font.render(
                    "Lives: " + str(wave.player.lives), True, (255, 255, 255))
                win.blit(lives_text, (int(20), 20))
            else:
                lose_text = font.render("You Lose", True, (255, 0, 0))
                lose_text = pygame.transform.scale2x(lose_text)
                win.blit(
                    lose_text,
                    (int((self.WINDOW_WIDTH - lose_text.get_width()) / 2),
                        int((self.WINDOW_HEIGHT - lose_text.get_height()) / 2))
                )

            # push updates to display
            pygame.display.update()

        pygame.font.quit()
        pygame.quit()
