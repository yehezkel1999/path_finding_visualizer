
from abc import ABC, abstractmethod
from typing import Tuple
from src.core.Grid import Grid
from src.core.Node import Node
import pygame


class PathFindingAlgorithm(ABC):
    return_key = pygame.K_ESCAPE

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

    def _pre_run(self) -> None:
        """
        method to call before an algorithm run
        :return: no return value
        """
        self._grid.reset()
        self._grid.update_nodes()  # update nodes depending on barrier locations

    @abstractmethod
    def run(self):
        pass
