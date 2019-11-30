import pygame


class Block:

    def __init__(self, pos_x, pos_y, width, height, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.WIDTH = width
        self.HEIGHT = height
        self.COLOR = color
        self.alive = True

    def draw(self, win):
        """ Add a block surface onto win, centred on its position """
        if self.alive:
            pygame.draw.rect(
                win,
                self.COLOR,
                (int(self.pos_x - self.WIDTH/2),
                    int(self.pos_y - self.HEIGHT/2),
                    self.WIDTH,
                    self.HEIGHT)
            )

    def check_if_hit(self, projectiles):
        """ Block can be destroyed by a Projectile object. If the block is hit 
        by a projectile(s), the projectile(s) is/are removed.
        """
        remove = False
        if self.alive:  # only check for collisions if entity is still alive
            to_remove = []
            for projectile in projectiles:
                if ((self.pos_x - self.WIDTH/2 <= projectile.pos_x <= self.pos_x + self.WIDTH/2)
                        and (self.pos_y - self.HEIGHT/2 <= projectile.pos_y <= self.pos_y + self.HEIGHT/2)):
                    to_remove.append(projectile)
                    remove = True
                    alive = False
            for proj in to_remove:
                projectiles.remove(proj)
            if remove:
                self.alive = False

    def update(self, projectiles):
        """ defines what the block entity does every frame """
        if self.alive:
            self.check_if_hit(projectiles)

    @staticmethod
    def update_all(blocks, projectiles):
        for block in blocks:
            block.update(projectiles)

    @staticmethod
    def draw_all(win, blocks):
        for block in blocks:
            block.draw(win)
