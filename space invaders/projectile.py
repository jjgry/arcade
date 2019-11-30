import pygame


class Projectile:
    HEIGHT = 10
    WIDTH = 2
    COLOR = (255, 255, 255)
    VELOCITY = 3

    def __init__(self, pos_x, pos_y, up: 'boolean'):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = up

    def draw(self, win):
        """ Add a projectile surface onto win, centred on its position """
        pygame.draw.rect(
            win,
            Projectile.COLOR,
            (int(self.pos_x - Projectile.WIDTH/2),
                int(self.pos_y - Projectile.HEIGHT/2),
                Projectile.WIDTH,
                Projectile.HEIGHT)
        )

    def update(self, projectiles, window_height):
        """ Called once for every frame to render """
        if self.direction == True:
            self.pos_y -= Projectile.VELOCITY
        else:
            self.pos_y += Projectile.VELOCITY
        self.remove_offscreen(projectiles, window_height)

    def remove_offscreen(self, projectiles, window_height):
        if ((self.pos_y < 0) or (self.pos_y > window_height)):
            projectiles.remove(self)

    @staticmethod
    def update_all(projectiles, window_height):
        for projectile in projectiles:
            projectile.update(projectiles, window_height)

    @staticmethod
    def draw_all(win, projectiles):
        for projectile in projectiles:
            projectile.draw(win)
