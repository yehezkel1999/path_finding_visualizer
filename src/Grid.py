import pygame

from Node import Node
import colors


class Grid:
    def __init__(self, window, height, width, rows):
        """
        creates a grid with a [height, width] of a window with the given amount of rows, the
        columns will be deduced by [width / (height / rows)].
        :param window: the pygame window
        :param height: the height of the window
        :param width: the width of the window
        :param rows: amount of rows the grid will have
        """
        # pygame window
        self._window = window
        # dimensions of the pygame window
        self._height = height
        self._width = width

        self._grid = []

        self._cube_length = height // rows
        cols = width // self._cube_length

        # normal:
        for i in range(rows):
            self._grid.append([])
            for j in range(cols):
                self._grid[i].append(Node(window, i, j, self._cube_length))

    @property
    def rows(self):
        return len(self._grid)

    @property
    def columns(self):
        return len(self._grid[0])

    def __getitem__(self, index) -> list:
        """
        operator[]
        :param index: index of the row (from 0 ro [rows])
        :return: a list that holds the row number of the given index
        """
        return self._grid[index]

    def __draw_lines(self):
        for i in range(self.rows):
            pygame.draw.line(self._window, colors.GREY,
                             (0, i * self._cube_length), (self._width, i * self._cube_length))
        for i in range(self.columns):
            pygame.draw.line(self._window, colors.GREY,
                             (i * self._cube_length, 0), (i * self._cube_length, self._height))

    def draw(self):
        self._window.fill(colors.WHITE)

        for row in self._grid:
            for node in row:
                node.draw()

        self.__draw_lines()
        pygame.display.update()

    def reset(self):
        self._window.fill(colors.WHITE)
        self.__draw_lines()

        for i in range(self.rows):
            for j in range(self.columns):
                self._grid[i][j].reset()

        pygame.display.update()

    def clicked_position(self, pos):
        x, y = pos

        row = y // self._cube_length
        col = x // self._cube_length

        return row, col

    def get_node_from_click(self) -> Node:
        row, col = self.clicked_position(pygame.mouse.get_pos())
        return self._grid[col][row]

    def update_nodes(self):
        for row in self._grid:
            for node in row:
                node.update_neighbors(self)
