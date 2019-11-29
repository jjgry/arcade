import pygame
from projectile import Projectile
from living_entity import LivingEntity

class Enemy(LivingEntity):

    def __init__(self, pos_x, pos_y):
        """ Enemies are entities with one life """
        super().__init__(pos_x, pos_y, 1)

    def fire_projectile(self):
        """ return a Projectile object travelling downwards """
        return Projectile(self.pos_x, self.pos_y, False)
