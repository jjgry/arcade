import pygame
from projectile import Projectile
from living_entity import LivingEntity

class Player(LivingEntity):
    VELOCITY = 10

    def __init__(self, pos_x, pos_y):
        """ Players are entities with three lives """
        super().__init__(pos_x, pos_y, 3)

    def fire_projectile(self):
        """ return a Projectile object travelling upwards """
        return Projectile(self.pos_x, self.pos_y, True)

    def move(self, keys, width):
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (self.pos_x > 0):
            self.pos_x -= Player.VELOCITY
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (self.pos_x < width - self.WIDTH):
            self.pos_x += Player.VELOCITY