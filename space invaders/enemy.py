import pygame
from projectile import Projectile
# from living_entity import LivingEntity

class Enemy:
    HEIGHT = 20
    WIDTH = 20
    LIVES = 1
    COLOR = (255, 255, 255)

    def __init__(self, pos_x, pos_y, delay_between_shots):
        """ Enemies are entities with one life """
        self.alive = True
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.delay_between_shots = delay_between_shots
        self.count = 0
        self.lives = Enemy.LIVES
    
    def draw(self, win):
        """ Add an entity surface onto win, centred on its position """
        if self.alive:
            pygame.draw.rect(
                win, 
                Enemy.COLOR,
                (int(self.pos_x - Enemy.WIDTH/2), 
                    int(self.pos_y - Enemy.HEIGHT/2), 
                    Enemy.WIDTH, 
                    Enemy.HEIGHT)
            )

    def fire_projectile(self):
        """ return a Projectile object travelling downwards """
        return Projectile(self.pos_x, self.pos_y, False)

    def check_if_hit(self, projectiles):
        """ Enemy can only be hit by a Projectile object travelling upwards.
        If the player is hit by a projectile(s), the projectile(s) is/are
        removed.

        Returns true if the player is hit.
        """
        hit = False
        if self.alive: # only check for collisions if entity is still alive
            to_remove = []
            for projectile in projectiles:
                if ((self.pos_x - 10 <= projectile.pos_x <= self.pos_x + self.WIDTH + 10)
                        and (self.pos_y - 10 <= projectile.pos_y <= self.pos_y + self.HEIGHT + 10)
                        and (projectile.direction == True)):
                    to_remove.append(projectile)
                    hit = True
            for proj in to_remove:
                projectiles.remove(proj)
            if hit:
                self.lives -= 1
                if self.lives <= 0:
                    self.alive = False
        return hit

    def move(self, keys, window_width, projectiles):
        """ defines what the player entity does every frame 

        returns an updated list of projectiles in the window
        """
        if self.alive:
            self.alive = not self.check_if_hit(projectiles)
            
            if self.count == 0:
                self.count = self.delay_between_shots
                potential_projectile = self.fire_projectile()
                if potential_projectile is not None:
                    projectiles.append(potential_projectile)
            else:
                self.count -= 1 
