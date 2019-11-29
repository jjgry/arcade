import pygame
from projectile import Projectile

class LivingEntity:
    HEIGHT = 20
    WIDTH = 20

    def __init__(self, pos_x, pos_y, lives, color=(255, 255, 255)):
        self.alive = True
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lives = lives
        self.color = color

    def draw(self, win):
        """ Add an entity surface onto win, centred on its position """
        if self.alive:
            pygame.draw.rect(
                win, 
                self.color,
                (int(self.pos_x - LivingEntity.WIDTH/2), 
                    int(self.pos_y - LivingEntity.HEIGHT/2), 
                    LivingEntity.WIDTH, 
                    LivingEntity.HEIGHT)
            )

    def fire_projectile(self):
        """Called when subclass wants for fire a projectile """
        raise NotImplementedError

    def hit(self):
        """ Called when an entiry is hit with a projectile """
        self.lives -= 1
        if self.lives <= 0:
            self.alive = False

