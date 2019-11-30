import pygame
import math
import random
from projectile import Projectile


class Enemy:
    WIDTH = 20
    HEIGHT = 20
    LIVES = 1
    COLOR = (255, 255, 255)
    DELAY_BETWEEN_SHOTS = 800
    MAX_DISPLACEMENT = 50
    MAX_PHASE = 800  # larger value leads to slower oscillation

    def __init__(self, pos_x, pos_y):
        """ Enemies are entities with one life """
        self.alive = True
        self.pos_x = pos_x
        self.original_pos_x = pos_x
        self.pos_y = pos_y
        self.count = int(Enemy.DELAY_BETWEEN_SHOTS * random.random())
        self.lives = Enemy.LIVES
        self.phase = 0

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
        If the enemy is hit by a projectile(s), the projectile(s) is/are
        removed.
        """
        hit = False
        if self.alive:  # only check for collisions if entity is still alive
            to_remove = []
            for projectile in projectiles:
                if ((self.pos_x - Enemy.WIDTH/2 <= projectile.pos_x <= self.pos_x + Enemy.WIDTH/2)
                        and (self.pos_y - Enemy.HEIGHT/2 <= projectile.pos_y <= self.pos_y + Enemy.HEIGHT/2)
                        and (projectile.direction == True)):
                    to_remove.append(projectile)
                    hit = True
            for proj in to_remove:
                projectiles.remove(proj)
            if hit:
                self.lives -= 1
                if self.lives <= 0:
                    self.alive = False

    def oscillate(self):
        """ updates the phase of the enemy and then updates the position
        based on the new phase
        """
        if self.phase == Enemy.MAX_PHASE:
            self.phase = 0
        else:
            self.phase += 1
        self.pos_x = self.original_pos_x + int(
            Enemy.MAX_DISPLACEMENT * math.sin(2 * math.pi * (self.phase / Enemy.MAX_PHASE)))

    def update(self, projectiles):
        """ defines what the player entity does every frame 

        returns an updated list of projectiles in the window
        """
        if self.alive:
            self.check_if_hit(projectiles)

            if self.count == 0:
                self.count = Enemy.DELAY_BETWEEN_SHOTS
                potential_projectile = self.fire_projectile()
                if potential_projectile is not None:
                    projectiles.append(potential_projectile)
            else:
                self.count -= 1

            self.oscillate()

    @staticmethod
    def update_all(enemies, projectiles):
        for enemy in enemies:
            enemy.update(projectiles)

    @staticmethod
    def draw_all(win, enemies):
        for enemy in enemies:
            enemy.draw(win)
