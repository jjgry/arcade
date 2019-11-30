import pygame
from enemy import Enemy
from player import Player
from projectile import Projectile
from block import Block
from wave import Wave

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

BLOCKS_SCREEN_POS = 350
BLOCK_STRUCTURE = [
        [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
        [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0], 
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1], 
    ]


def get_enemies():
    enemies = [
        Enemy(250, 200), 
        Enemy(300, 200)]
    return enemies


def get_blocks():
    blocks = []
    NUM_DEFENCES = 4
    spacing = 120
    total_width = (NUM_DEFENCES - 1) * spacing + len(BLOCK_STRUCTURE[0]) * Block.WIDTH
    left_offset = (WINDOW_WIDTH - total_width) / 2
    for i in range(NUM_DEFENCES):
        # draw one defence
        for y in range(len(BLOCK_STRUCTURE)):
            for x in range(len(BLOCK_STRUCTURE[0])):
                if BLOCK_STRUCTURE[y][x] == 1:
                    blocks.append(Block(
                        left_offset + spacing*i + x*Block.WIDTH, 
                        y*Block.HEIGHT + BLOCKS_SCREEN_POS))
    return blocks


def main():
    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Invaders")

    pygame.font.init()
    font = pygame.font.Font(pygame.font.get_default_font(), 20)

    player = Player(250, 450)
    enemies = get_enemies()
    blocks = get_blocks()
    projectiles = []
    wave = Wave(blocks, enemies, player, projectiles, WINDOW_WIDTH, WINDOW_HEIGHT)

    run = True
    while run:
        pygame.time.delay(3)  # pause for some number of ms

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # update everything
        wave.update(keys)

        # draw everything
        win.fill((0, 0, 0))
        wave.draw(win)
        lives_text = font.render(
            "Lives: " + str(player.lives), True, (255, 255, 255))
        win.blit(lives_text, (int(20), 20))

        # push updates to display
        pygame.display.update()

    pygame.font.quit()
    pygame.quit()


if __name__ == "__main__":
    main()
