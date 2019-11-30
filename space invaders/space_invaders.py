import pygame
from enemy import Enemy
from player import Player
from projectile import Projectile

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
DELAY_BETWEEN_PLAYER_SHOTS = 30
DELAY_BETWEEN_ENEMY_SHOTS = 200

def main():
    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Invaders") 

    player = Player(250, 450, DELAY_BETWEEN_PLAYER_SHOTS)
    enemy = Enemy(250, 200, DELAY_BETWEEN_ENEMY_SHOTS)
    projectiles = []

    run = True
    while run:    
        pygame.time.delay(10) # pause for 10ms (~100fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # update everything
        player.move(keys, WINDOW_WIDTH, projectiles)
        enemy.move(keys, WINDOW_WIDTH, projectiles)
        
        Projectile.remove_offscreen(projectiles, WINDOW_WIDTH, WINDOW_HEIGHT)
        Projectile.move_all(projectiles)

        # draw everything
        win.fill((0, 0, 0))

        player.draw(win)
        enemy.draw(win)

        for projectile in projectiles:
            projectile.draw(win)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
