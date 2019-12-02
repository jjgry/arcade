import sys
from pong.pong import Pong
from space_invaders.space_invaders import SpaceInvaders
from pacman.pacman import Pacman


def main():
    prog = sys.argv[1]

    if prog == "pong":
        Pong.start()
    elif prog == "space_invaders" or prog == "space":
        SpaceInvaders.start()
    elif prog == "pacman":
        Pacman()
    else:
        print("Incorrect arguments supplied.\n"
            + "Expected use: python main.py {pong/space_invaders/pacman}")


if __name__ == "__main__":
    main()
