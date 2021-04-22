from typing import Tuple, List

import pygame
import colors


class Node:

    # Grid color constants:
    blank = colors.WHITE
    barrier = colors.BLACK

    open = colors.NAVY_BLUE
    closed = colors.CYAN

    start = colors.ORANGE
    end = colors.ORANGE_RED

    checked = colors.MIDNIGHT_PURPLE
    looked = colors.MIDNIGHT_BLUE

    path = colors.YELLOW

    def __init__(self, window, row, col, length):
        # pygame window
        self._window = window

        self._row = row
        self._col = col

        self._length = length

        self._color = Node.blank

        self._neighbors = []

    @property
    def position(self):
        return self._col, self._row

    @property
    def window_x(self):
        return self._row * self._length

    @property
    def window_y(self):
        return self._col * self._length

    @property
    def color(self) -> Tuple[int, int, int]:
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def neighbors(self):
        return self._neighbors

    def reset(self):
        self._color = Node.blank

    def draw(self):
        pygame.draw.rect(self._window, self._color, (self.window_x, self.window_y, self._length, self._length))

    def update_neighbors(self, grid):
        self._neighbors.clear()
        if self._row < grid.rows - 1 and grid[self._row + 1][self._col].color != Node.barrier:  # down
            self._neighbors.append(grid[self._row + 1][self._col])
        if self._row > 0 and grid[self._row - 1][self._col].color != Node.barrier:  # up
            self._neighbors.append(grid[self._row - 1][self._col])
        if self._col < grid.columns - 1 and grid[self._row][self._col + 1].color != Node.barrier:  # right
            self._neighbors.append(grid[self._row][self._col + 1])
        if self._col > 0 and grid[self._row][self._col - 1].color != Node.barrier:  # left
            self._neighbors.append(grid[self._row][self._col - 1])

    def __lt__(self, other):
        return False
