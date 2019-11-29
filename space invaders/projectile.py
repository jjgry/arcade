import pygame

class Projectile:
    HEIGHT = 10
    WIDTH = 2
    COLOR = (255, 255, 255)
    VELOCITY = 5

    def __init__(self, pos_x, pos_y, up:'boolean'):
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
    
    def move(self):
        """ Called once for every frame to render """
        if self.direction == True:
            self.pos_y -= Projectile.VELOCITY