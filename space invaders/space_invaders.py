import pygame
from enemy import Enemy
from player import Player
from projectile import Projectile

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

def main():
    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Space Invaders") 

    player = Player(250, 450)

    run = True
    while run:    
        pygame.time.delay(10) # pause for 10ms (~100fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        # update everything

        player.move(keys, WINDOW_WIDTH)



        # draw everything

        win.fill((0, 0, 0))
        player.draw(win)


        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()