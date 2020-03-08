import pygame
import random
from copy import copy, deepcopy


class GameOfLife:

    GAME_WIDTH = 500
    GAME_HEIGHT = 500

    ALIVE_COLOR = (255, 255, 255)
    DEAD_COLOR = (0, 0, 0)

    FPS = 60  # the rate that the window updates

    def __init__(self, win):
        """ Initialise pygame and then execute loop until player closes window """
        pygame.init()
        pygame.display.set_caption("Game of Life")
        game_surface = pygame.Surface(
            (self.GAME_WIDTH, self.GAME_HEIGHT), pygame.RESIZABLE)
        clock = pygame.time.Clock()

        self.x_dimension = 20
        self.y_dimension = 20
        self.cell_size = 25
        self.rate = 1  # the rate at which the animation progresses
        self.last_rate = 1 # used for pause mechanics

        self.grid = GameOfLife.make_random_grid(
            self.x_dimension, self.y_dimension)

        frameCount = 0

        run = True
        while run:
            clock.tick(self.FPS)
            frameCount += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.VIDEORESIZE:
                    win = pygame.display.set_mode(
                        (event.w, event.h), pygame.RESIZABLE)
                    self.window_width = event.w
                    self.window_height = event.h

            keys_pressed = pygame.key.get_pressed()
            if keys_pressed[pygame.K_1]:
                self.rate = 1
                frameCount = 0
            if keys_pressed[pygame.K_2]:
                self.rate = 2
                frameCount = 0
            if keys_pressed[pygame.K_3]:
                self.rate = 3
                frameCount = 0
            if keys_pressed[pygame.K_SPACE]:
                if self.rate == 0:
                    self.rate = self.last_rate
                else:
                    self.last_rate = self.rate
                    self.rate = 0
                frameCount = 0
                continue

            if (self.rate != 0) and (frameCount * self.rate) % self.FPS == 0:
                frameCount = 0
                self.grid = GameOfLife.update_grid(self.grid)
                self.draw_grid(win)
                pygame.display.update()

        pygame.quit()

    @classmethod
    def make_random_grid(cls, x_dimension, y_dimension):
        return [[random.choice([True, False]) for _ in range(x_dimension)] for _ in range(y_dimension)]

    @classmethod
    def update_grid(cls, grid):
        newGrid = [[False for _ in range(len(grid[0]))]
                   for _ in range(len(grid))]
        for x in range(len(grid[0])):
            for y in range(len(grid)):  # for each cell in the row
                alive = grid[y][x]
                num_neighbours = GameOfLife.num_neighbours(grid, x, y)
                if alive and (num_neighbours == 2 or num_neighbours == 3):
                    newGrid[y][x] = True
                elif num_neighbours == 3:
                    newGrid[y][x] = True
        return newGrid

    @classmethod
    def num_neighbours(cls, grid, x, y):
        count = 0
        for x_lookup in range(x-1, x+2):
            for y_lookup in range(y-1, y+2):
                if (not (x_lookup < 0
                         or x_lookup >= len(grid[0])
                         or y_lookup < 0
                         or y_lookup >= len(grid))):
                    if grid[y_lookup][x_lookup]:
                        count += 1
        return count

    def draw_grid(self, win):
        for y in range(self.y_dimension):
            for x in range(self.x_dimension):
                color = self.ALIVE_COLOR if self.grid[y][x] else self.DEAD_COLOR
                pygame.draw.rect(
                    win,
                    color,
                    pygame.Rect(x * self.cell_size,
                                y * self.cell_size,
                                self.cell_size,
                                self.cell_size)
                )
