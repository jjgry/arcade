import sys
import pygame
from pong.pong import Pong
from space_invaders.space_invaders import SpaceInvaders
from pacman.pacman import Pacman

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

def main():
    prog = sys.argv[1]

    pygame.init()
    win = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Arcade")

    if prog == "pong":
        Pong(win)
    elif prog == "space_invaders" or prog == "space":
        SpaceInvaders(win)
    elif prog == "pacman":
        Pacman(win)
    else:
        print("Incorrect arguments supplied.\n"
              + "Expected use: python main.py {pong|space_invaders|pacman}")


if __name__ == "__main__":
    main()
