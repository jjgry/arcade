import pygame
from projectile import Projectile
from living_entity import LivingEntity

class Player(LivingEntity):
    VELOCITY = 5

    def __init__(self, pos_x, pos_y, delay_between_shots):
        """ Players are entities with three lives """
        super().__init__(pos_x, pos_y, 3, delay_between_shots)

    def fire_projectile(self):
        """ return a Projectile object travelling upwards """
        return Projectile(self.pos_x, self.pos_y, True)

    def move(self, keys, window_width, projectiles):
        """ defines what the player entity does every frame 

        returns an updated list of projectiles in the window
        """
        if ((keys[pygame.K_a] or keys[pygame.K_LEFT]) 
                and (self.pos_x > self.WIDTH)):
            self.pos_x -= Player.VELOCITY
        if ((keys[pygame.K_d] or keys[pygame.K_RIGHT]) 
                and (self.pos_x < window_width - self.WIDTH)):
            self.pos_x += Player.VELOCITY

        self.check_if_hit(projectiles)


        if self.count == 0:
            if (keys[pygame.K_SPACE]):
                self.count = self.delay_between_shots
                potential_projectile = self.fire_projectile()
                if potential_projectile is not None:
                    projectiles.append(potential_projectile)
        else:
            self.count -= 1 