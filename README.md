# arcade

Project written in [Python 3.8](https://www.python.org/) using [pygame 1.9.6](https://www.pygame.org/).

This is my attempt to become more familiar with Python 3. I have been using pygame as it is well documented and is adequate for the needs of these games.

My ultimate goal is to combine the individual games I have constructed here into an arcade machine with multiple games that a user can select between. Improved graphics and instructional menus would be a part of this.

N.B. the choppy look of the GIF's below is purely a consequence of the file format limitations. In reality these programs run at ~80fps.

## pong

My version of Pong (trademark held by [Atari Interactive Inc.](https://www.atari.com/)) currently consists of one `pong.py` module which can be executed to run the game. The game is designed for two players. Player 1 can operate their paddle using the `W` and `S` keys, whilst player 2 can do so with the `UP ARROW` and `DOWN ARROW` keys.

<p align="center">
  <img width="300" height="300" src="/pong/pong_demo.gif">
</p>

## space invaders

My version of Space Invaders (copyright held by [Taito Corporation](http://www.taito.com/)) is made using multiple modules and classes. The main module is `space_invaders.py` which can be executed to run the game. The player can move using the `A` and `D` keys or using the `LEFT ARROW` and `RIGHT ARROW` keys, and shoot using the `SPACE` bar.

<p align="center">
  <img width="300" height="300" src="/space invaders/space_invaders_demo.gif">
</p>

In the future I would like to implement a scoreboard, as well as the aliens progressively moving down the screen.
