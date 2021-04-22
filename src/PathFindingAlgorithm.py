
from abc import abstractmethod
from typing import Tuple

from Grid import Grid
from Node import Node


class PathFindingAlgorithm:
    def __init__(self, grid: Grid, start: Node, end: Node):
        self._grid = grid
        self._start = start
        self._end = end

        self._came_from = {}  # dictionary to keep track of where each node came from to eventually determine the path

    def _exclude_start_end(self, node: Node, color: Tuple[int, int, int]):
        if node is not self._start and node is not self._end:
            node.color = color

    def _construct_path(self):
        current: Node = self._end
        current.color = Node.end
        while current in self._came_from:
            current = self._came_from[current]
            self._exclude_start_end(current, Node.path)
            self._grid.draw()

    @abstractmethod
    def run(self):
        pass
