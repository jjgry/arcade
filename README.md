# arcade

Project written in [Python 3.8](https://www.python.org/) using [pygame 1.9.6](https://www.pygame.org/).

This is my attempt to become more familiar with Python 3. I have been using pygame as it is well documented and is adequate for the needs of these games.

My ultimate goal is to combine the individual games I have constructed here into an arcade machine with multiple games that a user can select between. Improved graphics and instructional menus would be a part of this.

## running the code

The primary module is `main.py` which can be ran with the name of the game you want to play - `{pong|space_invaders|pacman}`. eg. `python main.py pong`. Instructions on how to play the games is given below.

## the games so far

### pong

My version of Pong (trademark held by [Atari Interactive Inc.](https://www.atari.com/)) currently consists of one `pong.py` module which contains the class `Pong` which can be instantiated to start the game. The game is designed for two players. Player 1 can operate their paddle using the `W` and `S` keys, whilst player 2 can do so with the `UP ARROW` and `DOWN ARROW` keys.

<p align="center">
  <img width="300" height="300" src="/pong/pong_demo.gif">
</p>

### space invaders

My version of Space Invaders (copyright held by [Taito Corporation](http://www.taito.com/)) is made using multiple modules and classes. The main module is `space_invaders.py` which contains the class `SpaceInvaders` which is instantiated to start the game. The player can move using the `A` and `D` keys or using the `LEFT ARROW` and `RIGHT ARROW` keys, and shoot using the `SPACE` bar.

<p align="center">
  <img width="300" height="300" src="/space_invaders/space_invaders_demo.gif">
</p>

In the future I would like to implement a scoreboard, as well as the aliens progressively moving down the screen.

### pacman

I have started but there is no real functionality yet.

## notes

* The choppy look of the GIF's below is purely a consequence of the file format limitations. In reality these programs run at 120fps, with the ability to run much faster if it were so desired.
* This project is very much a work in progress, and as much as I try to update this document to reflect the changes I am making, it is not always consistent with the code.
