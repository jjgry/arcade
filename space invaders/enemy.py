import pygame
import random
from projectile import Projectile
# from living_entity import LivingEntity


class Enemy:

    def __init__(self, pos_x, pos_y, width, height, lives, color, delay_between_shots):
        """ Enemies are entities with one life """
        self.alive = True
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.WIDTH = width
        self.HEIGHT = height
        self.lives = lives
        self.COLOR = color
        self.DELAY_BETWEEN_SHOTS = delay_between_shots
        self.count = int(delay_between_shots * random.random())

    def draw(self, win):
        """ Add an entity surface onto win, centred on its position """
        if self.alive:
            pygame.draw.rect(
                win,
                self.COLOR,
                (int(self.pos_x - self.WIDTH/2),
                    int(self.pos_y - self.HEIGHT/2),
                    self.WIDTH,
                    self.HEIGHT)
            )

    def fire_projectile(self):
        """ return a Projectile object travelling downwards """
        return Projectile(self.pos_x, self.pos_y, False)

    def check_if_hit(self, projectiles):
        """ Enemy can only be hit by a Projectile object travelling upwards.
        If the enemy is hit by a projectile(s), the projectile(s) is/are
        removed.
        """
        hit = False
        if self.alive:  # only check for collisions if entity is still alive
            to_remove = []
            for projectile in projectiles:
                if ((self.pos_x - self.WIDTH/2 <= projectile.pos_x <= self.pos_x + self.WIDTH/2)
                        and (self.pos_y - self.HEIGHT/2 <= projectile.pos_y <= self.pos_y + self.HEIGHT/2)
                        and (projectile.direction == True)):
                    to_remove.append(projectile)
                    hit = True
            for proj in to_remove:
                projectiles.remove(proj)
            if hit:
                self.lives -= 1
                if self.lives <= 0:
                    self.alive = False

    def update(self, projectiles):
        """ defines what the player entity does every frame 

        returns an updated list of projectiles in the window
        """
        if self.alive:
            self.check_if_hit(projectiles)

            if self.count == 0:
                self.count = self.DELAY_BETWEEN_SHOTS
                potential_projectile = self.fire_projectile()
                if potential_projectile is not None:
                    projectiles.append(potential_projectile)
            else:
                self.count -= 1

    @staticmethod
    def update_all(enemies, projectiles):
        for enemy in enemies:
            enemy.update(projectiles)

    @staticmethod
    def draw_all(win, enemies):
        for enemy in enemies:
            enemy.draw(win)
