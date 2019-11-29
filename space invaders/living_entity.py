import pygame
from projectile import Projectile

class LivingEntity:
    HEIGHT = 20
    WIDTH = 20

    def __init__(self, pos_x, pos_y, lives, delay_between_shots, color=(255, 255, 255)):
        self.alive = True
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lives = lives
        self.delay_between_shots = delay_between_shots
        self.color = color
        self.count = 0

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

    def check_if_hit(self, projectiles):
        """ Checks whether the entity has been hit by any of the projectiles, 
        updating state as necessary. Being hit by multiple projectiles will 
        have the same effect as being hit by one.

        Returns true of entity was hit
        """
        hit = False
        if self.alive: # only check for collisions if entity is still alive

            for projectile in projectiles:
                if ((self.pos_x <= projectile.pos_x <= self.pos_x + self.WIDTH)
                        and (self.pos_y <= projectile.pos_y <= self.pos_y + self.HEIGHT)):
                    projectiles.remove(projectile)
                    hit = True

            if hit:
                self.lives -= 1
                if self.lives <= 0:
                    self.alive = False
        
        return hit
