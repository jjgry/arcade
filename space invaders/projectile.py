import pygame


class Projectile:
    WIDTH = 5
    HEIGHT = 20
    COLOR = (145, 145, 145)
    DAMAGE = 2

    def __init__(self, pos_x, pos_y, up: 'boolean', velocity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocity = velocity
        self.direction = up
        self.damage = self.DAMAGE

    def draw(self, win):
        """ Add a projectile surface onto win, centred on its position """
        pygame.draw.rect(
            win,
            Projectile.COLOR,
            (int(self.pos_x - self.WIDTH/2),
                int(self.pos_y - self.HEIGHT/2),
                self.WIDTH,
                self.HEIGHT)
        )

    def update(self, projectiles, window_height):
        """ Called once for every frame to render """
        if self.direction == True:
            self.pos_y -= self.velocity
        else:
            self.pos_y += self.velocity
        self.remove_offscreen(projectiles, window_height)

    def remove_offscreen(self, projectiles, window_height):
        """ Check if the projectile is still on screen. Remove it from
        projectiles if it is not
        """
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
