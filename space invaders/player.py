import pygame
from projectile import Projectile
# from living_entity import LivingEntity


class Player:
    HEIGHT = 20
    WIDTH = 20
    VELOCITY = 3
    LIVES = 3
    COLOR = (255, 255, 255)

    def __init__(self, pos_x, pos_y, delay_between_shots):
        """ Players are entities with three lives """
        self.alive = True
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.delay_between_shots = delay_between_shots
        self.count = 0
        self.lives = Player.LIVES

    def draw(self, win):
        """ Add an entity surface onto win, centred on its position """
        if self.alive:
            pygame.draw.rect(
                win,
                Player.COLOR,
                (int(self.pos_x - Player.WIDTH/2),
                    int(self.pos_y - Player.HEIGHT/2),
                    Player.WIDTH,
                    Player.HEIGHT)
            )

    def fire_projectile(self):
        """ return a Projectile object travelling upwards """
        return Projectile(self.pos_x, self.pos_y, True)

    def check_if_hit(self, projectiles):
        """ Player can only be hit by a Projectile object travelling downwards.
        If the player is hit by a projectile(s), the projectile(s) is/are
        removed.
        """
        hit = False
        if self.alive:  # only check for collisions if entity is still alive

            for projectile in projectiles:
                if ((self.pos_x - Player.WIDTH/2 <= projectile.pos_x <= self.pos_x + Player.WIDTH/2)
                        and (self.pos_y - Player.HEIGHT/2 <= projectile.pos_y <= self.pos_y + Player.HEIGHT/2)
                        and (projectile.direction == False)):
                    projectiles.remove(projectile)
                    hit = True

            if hit:
                self.lives -= 1
                if self.lives <= 0:
                    self.alive = False

    def update(self, keys, window_width, projectiles):
        """ defines what the player entity does every frame """
        if self.alive:
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
