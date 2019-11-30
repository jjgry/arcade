import pygame
from enemy import Enemy
from player import Player
from projectile import Projectile
from block import Block

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
DELAY_BETWEEN_PLAYER_SHOTS = 30
DELAY_BETWEEN_ENEMY_SHOTS = 200


def get_enemies():
    enemies = [Enemy(250, 200, DELAY_BETWEEN_ENEMY_SHOTS),
               Enemy(300, 200, DELAY_BETWEEN_ENEMY_SHOTS)]
    return enemies


def get_blocks():
    blocks = []
    return blocks


def main():
    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    player = Player(250, 450, DELAY_BETWEEN_PLAYER_SHOTS)
    enemies = get_enemies()
    blocks = get_blocks()
    projectiles = []

    run = True
    while run:
        pygame.time.delay(10)  # pause for 10ms (~100fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # update everything
        player.update(keys, WINDOW_WIDTH, projectiles)
        Enemy.update_all(enemies, projectiles)
        Block.update_all(blocks, projectiles)
        Projectile.update_all(projectiles, WINDOW_HEIGHT)

        # draw everything
        win.fill((0, 0, 0))
        player.draw(win)
        Enemy.draw_all(win, enemies)
        Block.draw_all(win, blocks)
        Projectile.draw_all(win, projectiles)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
