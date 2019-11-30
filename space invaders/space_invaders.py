import pygame
from enemy import Enemy
from player import Player
from projectile import Projectile
from block import Block

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BLOCK_WIDTH = 20
BLOCK_HEIGHT = 20
BLOCK_COLOR = (255, 120, 120)

ENEMY_WIDTH = 20
ENEMY_HEIGHT = 20
ENEMY_LIVES = 1
ENEMY_COLOR = (255, 255, 255)
ENEMY_DELAY_BETWEEN_SHOTS = 400

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
PLAYER_VELOCITY = 3
PLAYER_LIVES = 3
PLAYER_COLOR = (255, 255, 255)
PLAYER_DELAY_BETWEEN_SHOTS = 40


def get_enemies():
    enemies = [
        Enemy(
            250,
            200,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            ENEMY_LIVES,
            ENEMY_COLOR,
            ENEMY_DELAY_BETWEEN_SHOTS),
        Enemy(
            300,
            200,
            ENEMY_WIDTH,
            ENEMY_HEIGHT,
            ENEMY_LIVES,
            ENEMY_COLOR,
            ENEMY_DELAY_BETWEEN_SHOTS)]
    print(len(enemies))
    return enemies


def get_blocks():
    blocks = []
    num_blocks = int(WINDOW_WIDTH / 20) - 1
    for i in range(num_blocks):
        blocks.append(Block(
            (i+1)*BLOCK_WIDTH,
            350,
            BLOCK_WIDTH,
            BLOCK_HEIGHT,
            BLOCK_COLOR))
    return blocks


def update(keys, player, enemies, blocks, projectiles):
    player.update(keys, WINDOW_WIDTH, projectiles)
    Enemy.update_all(enemies, projectiles)
    Block.update_all(blocks, projectiles)
    Projectile.update_all(projectiles, WINDOW_HEIGHT)


def draw_entities(win, player, enemies, blocks, projectiles):
    win.fill((0, 0, 0))
    player.draw(win)
    Enemy.draw_all(win, enemies)
    Block.draw_all(win, blocks)
    Projectile.draw_all(win, projectiles)


def main():
    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 20)

    player = Player(
        250,
        450,
        PLAYER_WIDTH,
        PLAYER_HEIGHT,
        PLAYER_VELOCITY,
        PLAYER_LIVES,
        PLAYER_COLOR,
        PLAYER_DELAY_BETWEEN_SHOTS)
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
        update(keys, player, enemies, blocks, projectiles)

        # draw everything
        draw_entities(win, player, enemies, blocks, projectiles)
        lives_text = font.render(
            "Lives: " + str(player.lives), True, (255, 255, 255))
        win.blit(lives_text, (int(20), 20))

        pygame.display.update()

    pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
