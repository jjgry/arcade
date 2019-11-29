import pygame
from projectile import Projectile
from living_entity import LivingEntity

class Enemy(LivingEntity):

    def __init__(self, pos_x, pos_y, delay_between_shots):
        """ Enemies are entities with one life """
        super().__init__(pos_x, pos_y, 1, delay_between_shots)
        

    def fire_projectile(self):
        """ return a Projectile object travelling downwards """
        return Projectile(self.pos_x, self.pos_y, False)

    def move(self, keys, window_width, projectiles):
        """ defines what the player entity does every frame 

        returns an updated list of projectiles in the window
        """
        alive = self.check_if_hit(projectiles)

        if self.count == 0:
            if (keys[pygame.K_SPACE]):
                self.count = self.delay_between_shots
                potential_projectile = self.fire_projectile()
                if potential_projectile is not None:
                    projectiles.append(potential_projectile)
        else:
            self.count -= 1 
