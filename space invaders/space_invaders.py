import pygame
from enemy import Enemy
from player import Player
from projectile import Projectile
from block import Block
from wave import Wave


class SpaceInvaders:

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

    def __init__(self):
        self.player = Player(250, 450)
        self.enemies = self.get_enemies()
        self.blocks = self.get_blocks()
        self.projectiles = []

    @staticmethod
    def start():
        space_invaders = SpaceInvaders()
        space_invaders.run()

    def get_enemies(self):
        enemies = [
            Enemy(250, 200),
            Enemy(300, 200)]
        return enemies

    def get_blocks(self):
        blocks = []
        NUM_DEFENCES = 4
        spacing = 120
        total_width = (NUM_DEFENCES - 1) * spacing + \
            len(self.BLOCK_STRUCTURE[0]) * Block.WIDTH
        left_offset = (self.WINDOW_WIDTH - total_width) / 2
        for i in range(NUM_DEFENCES):
            # draw one defence
            for y in range(len(self.BLOCK_STRUCTURE)):
                for x in range(len(self.BLOCK_STRUCTURE[0])):
                    if self.BLOCK_STRUCTURE[y][x] == 1:
                        blocks.append(Block(
                            left_offset + spacing*i + x*Block.WIDTH,
                            y*Block.HEIGHT + self.BLOCKS_SCREEN_POS))
        return blocks

    def run(self):
        pygame.init()
        win = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Space Invaders")

        pygame.font.init()
        font = pygame.font.Font(pygame.font.get_default_font(), 20)

        wave = Wave(self.blocks, self.enemies, self.player, self.projectiles,
                    self.WINDOW_WIDTH, self.WINDOW_HEIGHT)

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
                "Lives: " + str(self.player.lives), True, (255, 255, 255))
            win.blit(lives_text, (int(20), 20))

            # push updates to display
            pygame.display.update()

        pygame.font.quit()
        pygame.quit()


if __name__ == "__main__":
    SpaceInvaders.start()
