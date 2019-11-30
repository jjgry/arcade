import pygame
from block import Block
from enemy import Enemy
from player import Player
from projectile import Projectile


class Wave:
    """ A wave holds all of the state of the enemies, projectiles and player
    on the screen at any given time
    """

    def __init__(self, blocks, enemies, player, projectiles, WINDOW_WIDTH, WINDOW_HEIGHT):
        self.enemies = enemies
        self.blocks = blocks
        self.player = player
        self.projectiles = projectiles
        self.WINDOW_WIDTH = WINDOW_WIDTH
        self.WINDOW_HEIGHT = WINDOW_HEIGHT

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