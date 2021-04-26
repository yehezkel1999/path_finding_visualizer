
import pygame
from queue import Queue
from ..core.Grid import Grid
from ..core.Node import Node
from ..core.PathFindingAlgorithm import PathFindingAlgorithm


class BFS(PathFindingAlgorithm):
    run_key = pygame.K_b

    def __init__(self, grid: Grid, start: Node, end: Node):
        super().__init__(grid, start, end)
        self.queue = Queue()
        self.queue.put(start)
        # a dictionary that is in sync with open_set simply to keep track of what's in open_set
        self.queue_hash = {start}

    def run(self):
        super()._pre_run()
        while not self.queue.empty():
            for event in pygame.event.get():  # so the user can quit mid algorithm
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN and event.key == PathFindingAlgorithm.return_key:
                    return False

            current: Node = self.queue.get()  # the current node that is being checked

            if current is self._end:  # found path
                self._construct_path()
                return True

            for neighbor in current.neighbors:
                if neighbor not in self.queue_hash:
                    self.queue.put(neighbor)
                    self.queue_hash.add(neighbor)
                    self._came_from[neighbor] = current
                    self._exclude_start_end(neighbor, Node.open)

            self._exclude_start_end(current, Node.closed)  # considered the node and for now it's closed

            self._grid.draw()

        return False  # path not found
