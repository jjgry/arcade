import pygame
from block import Block
from enemy import Enemy
from player import Player
from projectile import Projectile


class Wave:
    """ A wave holds all of the state of the enemies, projectiles and player
    on the screen at any given time. It is also responsible for updating and 
    drawind all of these entities whenever it is called to do so.
    """
    EMEMIES_DIM = (6, 4)
    ENEMIES_X_SPACING = 50
    ENEMIES_Y_SPACING = 50

    DEFENCE_SCREEN_POS = 350
    DEFENCE_NUM = 3
    DEFENCE_SPACING = 120
    DEFENCE_STRUCTURE = [
        [0, 0, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
    ]

    def __init__(self, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT
        self.enemies = self.get_enemies()
        self.blocks = self.get_blocks()
        self.player = Player(250, 450)
        self.projectiles = []

    def update(self, keys):
        """ Update all objects in the wave """
        Block.update_all(self.blocks, self.projectiles)
        Enemy.update_all(self.enemies, self.projectiles)
        self.player.update(keys, self.WINDOW_WIDTH, self.projectiles)
        Projectile.update_all(self.projectiles, self.WINDOW_HEIGHT)

    def draw(self, win):
        """ Draw all objects in the wave to win """
        Block.draw_all(win, self.blocks)
        Enemy.draw_all(win, self.enemies)
        self.player.draw(win)
        Projectile.draw_all(win, self.projectiles)

    def get_enemies(self):
        """ Enemies are grouped into columns. Initialise so that only the 
        bottom-most enemy can fire.

        The returned array is such that enemies[0][3] is the enemy in the 1-st
        column and the 4-th row (1-st row is the top of screen)
        """
        enemies = []
        total_width = (self.EMEMIES_DIM[0] - 1) * \
            self.ENEMIES_X_SPACING + Enemy.WIDTH
        left_offset = (self.WINDOW_WIDTH - total_width) / 2
        for x in range(self.EMEMIES_DIM[0]):
            column = []
            for y in range(self.EMEMIES_DIM[1]):
                column.append(Enemy(
                    self.ENEMIES_X_SPACING * x + left_offset,
                    self.ENEMIES_Y_SPACING * y + 100,
                    False))
            enemies.append(column)
        for column in enemies:
            column[self.EMEMIES_DIM[1] - 1].can_fire = True
        return enemies

    def get_blocks(self):
        """ Return a list of blocks to be displayed. These blocks are arranged
        into multiple defences.
        """
        blocks = []
        total_width = (self.DEFENCE_NUM - 1) * self.DEFENCE_SPACING + \
            len(self.DEFENCE_STRUCTURE[0]) * Block.WIDTH
        left_offset = (self.WINDOW_WIDTH - total_width) / 2
        for i in range(self.DEFENCE_NUM):
            # draw one defence
            for y in range(len(self.DEFENCE_STRUCTURE)):
                for x in range(len(self.DEFENCE_STRUCTURE[0])):
                    if self.DEFENCE_STRUCTURE[y][x] == 1:
                        blocks.append(Block(
                            x * Block.WIDTH + self.DEFENCE_SPACING * i + left_offset,
                            y * Block.HEIGHT + self.DEFENCE_SCREEN_POS))
        return blocks
