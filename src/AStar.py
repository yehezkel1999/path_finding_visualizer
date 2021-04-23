
import pygame
from queue import PriorityQueue
from Grid import Grid
from Node import Node
from PathFindingAlgorithm import PathFindingAlgorithm


class AStar(PathFindingAlgorithm):
    def __init__(self, grid: Grid, start: Node, end: Node):
        super().__init__(grid, start, end)

        self.count = 0  # a counter for the nodes
        """
        3 type tuple priority queue:
        first: h score
        second: count, for determining which node was inserted first for tie breakers
        node: the actual node in the grid
        """
        self.open_set = PriorityQueue()
        self.open_set.put((0, self.count, start))
        # a dictionary that is in sync with open_set simply to keep track of what's in open_set
        self.open_set_hash = {start}

        """
        dictionary to store all of the g scores, where they all start at "infinity"
        the g score is simply the amount of nodes it takes to get from the start to each node
        """
        self.g_score = {node: float("inf") for row in grid for node in row}
        self.g_score[start] = 0

        """
        dictionary to store all of the f scores, where they all start at "infinity"
        the f score is simply the g score + the h score
        """
        self.f_score = {node: float("inf") for row in grid for node in row}
        # making a guess for the f score so it wouldn't be "infinity"
        self.f_score[start] = AStar._h_score(start, end)

    @staticmethod
    def _h_score(node1: Node, node2: Node) -> float:
        """
        the h score is a guess of how far node 2 is from node 1 using Manhattan distance.
        :return: the Manhattan distance.
        """
        x1, y1 = node1.position
        x2, y2 = node2.position
        return abs(x1 - x2) + abs(y1 - y2)

    def run(self):
        super()._pre_run()
        while not self.open_set.empty():
            for event in pygame.event.get():  # so the user can quit mid algorithm
                if event.type == pygame.QUIT:
                    pygame.quit()

            current: Node = self.open_set.get()[2]  # the current node that is being checked
            self.open_set_hash.remove(current)

            if current is self._end:  # found path
                self._construct_path()
                return True

            for neighbor in current.neighbors:
                neighbor_g_score = self.g_score[current] + 1  # getting to the neighbor from current takes one step

                if neighbor_g_score < self.g_score[neighbor]:  # if this is shorter than its current g score then update
                    self._came_from[neighbor] = current        # neighbor in all data structures
                    self.g_score[neighbor] = neighbor_g_score
                    self.f_score[neighbor] = neighbor_g_score + self._h_score(neighbor, self._end)

                    if neighbor not in self.open_set_hash:
                        self.count += 1
                        self.open_set.put((self.f_score[neighbor], self.count, neighbor))
                        self.open_set_hash.add(neighbor)
                        neighbor.color = Node.open

            self._grid.draw()

            self._exclude_start_end(current, Node.closed)  # considered the node and for now it's closed

        return False  # path not found
