import sys
import pygame
from pong.pong import Pong
from space_invaders.space_invaders import SpaceInvaders
from game_of_life.game_of_life import GameOfLife
from pacman.pacman import Pacman

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
INCORRECT_ARGS_MESSAGE = "Incorrect arguments supplied.\n" \
    + "Expected use: python main.py <game> where game is chosen from:\n" \
    + "\tpong\n" \
    + "\tspace_invaders\n" \
    + "\tpacman\n" \
    + "\tgol"


def main():
    prog = None
    if len(sys.argv) == 2:
        prog = sys.argv[1]
    else:
        print(INCORRECT_ARGS_MESSAGE)
        return

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
    elif prog == "game_of_life" or prog == "gol":
        GameOfLife(win)
    else:
        print(INCORRECT_ARGS_MESSAGE)
        return


if __name__ == "__main__":
    main()
