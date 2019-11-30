import pygame


class Block:
    WIDTH = 5
    HEIGHT = 5
    COLOR = (190, 90, 37)

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.alive = True

    def draw(self, win):
        """ Add a block surface onto win, centred on its position """
        pygame.draw.rect(
            win,
            Block.COLOR,
            (int(self.pos_x - Block.WIDTH/2),
                int(self.pos_y - Block.HEIGHT/2),
                Block.WIDTH,
                Block.HEIGHT)
        )

    def check_if_hit(self, projectiles):
        """ Block can be destroyed by a Projectile object. If the block is hit 
        by a projectile(s), the projectile(s) has it's damage value decremented
        and if the value is 1 it is removed.
        """
        to_remove = []
        for projectile in projectiles:
            if ((self.pos_x - Block.WIDTH/2 <= projectile.pos_x <= self.pos_x + Block.WIDTH/2)
                    and (self.pos_y - Block.HEIGHT/2 <= projectile.pos_y <= self.pos_y + Block.HEIGHT/2)):
                self.alive = False
                if projectile.damage <= 1:
                    to_remove.append(projectile)
                else:
                    projectile.damage -= 1
        for projectile in to_remove:
            projectiles.remove(projectile)

    def update(self, projectiles):
        """ defines what the block entity does every frame """
        if self.alive:
            self.check_if_hit(projectiles)

    @staticmethod
    def update_all(blocks, projectiles):
        to_remove = []
        for block in blocks:
            block.update(projectiles)
            if not block.alive:
                to_remove.append(block)
        for block in to_remove:
            blocks.remove(block)

    @staticmethod
    def draw_all(win, blocks):
        for block in blocks:
            block.draw(win)
