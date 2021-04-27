
import pygame
from collections import deque
from ..core.Grid import Grid
from ..core.Node import Node
from ..core.PathFindingAlgorithm import PathFindingAlgorithm


class DFS(PathFindingAlgorithm):
    run_key = pygame.K_d

    def __init__(self, grid: Grid, start: Node, end: Node):
        super().__init__(grid, start, end)
        self.stack = deque()
        self.stack.append(start)
        # a dictionary that is in sync with open_set simply to keep track of what's in open_set
        self.stack_hash = {start}

    def run(self):
        count = 0
        super()._pre_run()
        while self.stack:
            for event in pygame.event.get():  # so the user can quit mid algorithm
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                if event.type == pygame.KEYDOWN and event.key == PathFindingAlgorithm.return_key:
                    return False
            current: Node = self.stack.pop()  # the current node that is being checked

            if current is self._end:  # found path
                self._construct_path()
                return True

            for neighbor in current.neighbors:
                if neighbor not in self.stack_hash:
                    self.stack.append(neighbor)
                    self.stack_hash.add(neighbor)
                    self._came_from[neighbor] = current
                    self._exclude_start_end(neighbor, Node.open)
                if neighbor is self._end:
                    break

            self._exclude_start_end(current, Node.closed)  # considered the node and for now it's closed

            self._grid.draw()
            count += 1

        return False  # path not found
