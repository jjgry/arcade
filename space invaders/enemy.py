import pygame
import math
import random
from projectile import Projectile


class Enemy:
    WIDTH = 30
    HEIGHT = 30
    LIVES = 1
    COLOR = (129, 128, 14)
    DELAY_BETWEEN_SHOTS = 500
    MAX_DISPLACEMENT = 50
    MAX_PHASE = 1000  # larger value leads to slower oscillation
    PROJ_VELOCITY = 2

    def __init__(self, pos_x, pos_y, can_fire: 'boolean'):
        """ Enemies are entities with one life """
        self.alive = True
        self.pos_x = pos_x
        self.can_fire = can_fire
        self.original_pos_x = pos_x
        self.pos_y = pos_y
        self.count = int(Enemy.DELAY_BETWEEN_SHOTS * random.random())
        self.lives = Enemy.LIVES
        self.phase = 0

    def draw(self, win):
        """ Add an entity surface onto win, centred on its position """
        pygame.draw.rect(
            win,
            self.COLOR,
            (int(self.pos_x - Enemy.WIDTH/2),
                int(self.pos_y - Enemy.HEIGHT/2),
                Enemy.WIDTH,
                Enemy.HEIGHT)
        )

    def check_if_hit(self, enemies, projectiles):
        """ Enemy can only be hit by a Projectile object travelling upwards.
        If the enemy is hit by a projectile(s), the projectile(s) is/are
        removed, and note that the enemy above can now fire.

        We return the position of the enemy that can now fire.
        """
        hit = False
        to_remove = []
        for projectile in projectiles:
            if ((self.pos_x - Enemy.WIDTH/2 <= projectile.pos_x <= self.pos_x + Enemy.WIDTH/2)
                    and (self.pos_y - Enemy.HEIGHT/2 <= projectile.pos_y <= self.pos_y + Enemy.HEIGHT/2)
                    and (projectile.direction == True)):
                to_remove.append(projectile)
                hit = True
        for proj in to_remove:
            projectiles.remove(proj)

        now_can_fire = None
        if hit:
            self.alive = False
            self_pos = Enemy.find_index(enemies, self)
            if self_pos[0] != 0:  # if we are not already the top enemy
                any_lower = False  # any_lower will be set True if there are enemies below us still alive
                for index, other in enumerate(enemies[self_pos[0]]):
                    if (index > self_pos[1]) and (other.alive == True):
                        any_lower = True
                if not any_lower:
                    # find the next highest enemy by its index
                    # iterate over other in column
                    for y_index, other in enumerate(enemies[self_pos[0]]):
                        if (y_index < self_pos[1]) and (other.alive == True):
                            now_can_fire = other
        if now_can_fire is not None:
            now_can_fire.can_fire = True

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

    def update(self, enemies, projectiles):
        """ defines what an enemy entity does every frame """
        self.check_if_hit(enemies, projectiles)
        if self.can_fire:
            if self.count == 0:
                self.count = Enemy.DELAY_BETWEEN_SHOTS
                # projectile firing downwards
                projectiles.append(Projectile(
                    self.pos_x, self.pos_y, False, Enemy.PROJ_VELOCITY))
            else:
                self.count -= 1
        self.oscillate()

    @staticmethod
    def find_index(enemies, enemy):
        for i, column in enumerate(enemies):
            if enemy in column:
                return (i, column.index(enemy))

    @staticmethod
    def update_all(enemies, projectiles):
        for column in enemies:
            for enemy in column:
                if enemy.alive:
                    enemy.update(enemies, projectiles)

    @staticmethod
    def draw_all(win, enemies):
        for column in enemies:
            for enemy in column:
                if enemy.alive:
                    enemy.draw(win)
