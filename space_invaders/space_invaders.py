import pygame
from space_invaders.enemy import Enemy
from space_invaders.player import Player
from space_invaders.projectile import Projectile
from space_invaders.block import Block
from space_invaders.wave import Wave
from helper_code import scale


class SpaceInvaders:

    GAME_WIDTH = 500
    GAME_HEIGHT = 500

    FPS = 120

    def __init__(self, win):
        """ This is the top-level code for space invaders. We are passed a 
        window to draw into and do so continually until the user exits.
        """
        pygame.init()
        pygame.display.set_caption("Space Invaders")
        game_surface = pygame.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))
        clock = pygame.time.Clock()

        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 20)

        wave = Wave(self.GAME_WIDTH, self.GAME_HEIGHT)

        run = True
        while run:
            # pygame.time.delay(10)  # pause for some number of ms
            clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.VIDEORESIZE:
                    win = pygame.display.set_mode(
                        (event.w, event.h), pygame.RESIZABLE)
                    self.window_width = event.w
                    self.window_height = event.h

            keys = pygame.key.get_pressed()

            # update everything
            wave.update(keys)

            # draw everything
            game_surface.fill((0, 0, 0))
            if wave.player.lives > 0:
                wave.draw(game_surface)
                lives_text = font.render(
                    "Lives: " + str(wave.player.lives), True, (255, 255, 255))
                game_surface.blit(lives_text, (int(20), 20))
            else:
                lose_text = font.render("You Lose", True, (255, 0, 0))
                lose_text = pygame.transform.scale2x(lose_text)
                game_surface.blit(
                    lose_text,
                    (int((self.GAME_WIDTH - lose_text.get_width()) / 2),
                        int((self.GAME_HEIGHT - lose_text.get_height()) / 2))
                )

            scale(
                win,
                game_surface,
                (self.GAME_WIDTH, self.GAME_HEIGHT),
                (self.window_width, self.window_height))

            # push updates to display
            pygame.display.update()

        pygame.font.quit()
        pygame.quit()
