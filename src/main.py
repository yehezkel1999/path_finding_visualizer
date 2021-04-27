
import pygame
from src.core.Grid import Grid
from src.core.Node import Node
from src.algorithms.AStar import AStar
from src.algorithms.DFS import DFS
from src.algorithms.BFS import BFS

MOUSE_BUTTONS = 3  # find a way to figure this out

CUBE_LENGTH = 12
HEIGHT = 480
WIDTH = int(HEIGHT * 1.2)


def main():
    window = pygame.display.set_mode((HEIGHT, WIDTH))  # set up pygame window
    pygame.display.set_caption("Path Finding Visualizer")

    grid = Grid(window, HEIGHT, WIDTH, CUBE_LENGTH)
    loop(grid)

    pygame.quit()


def loop(grid: Grid):
    start = None
    end = None
    algorithm = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if pygame.mouse.get_pressed(MOUSE_BUTTONS)[0]:  # left click
                node = grid.get_node_from_click()
                if not start:
                    start = node
                    start.color = Node.start
                elif not end and node is not start:
                    end = node
                    end.color = Node.end
                elif node is not start and node is not end:
                    node.color = Node.barrier

            elif pygame.mouse.get_pressed(MOUSE_BUTTONS)[2]:  # right click
                node = grid.get_node_from_click()
                if node is start:
                    start = None
                elif node is end:
                    end = None

                node.clear()

            elif event.type == pygame.KEYDOWN:
                if event.key == AStar.run_key and start and end:
                    algorithm = AStar(grid, start, end)
                if event.key == BFS.run_key and start and end:
                    algorithm = BFS(grid, start, end)
                if event.key == DFS.run_key and start and end:
                    algorithm = DFS(grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid.clear()
        if algorithm:
            return_value = algorithm.run()
            if return_value is None:
                break
            algorithm = None
        grid.draw()


if __name__ == '__main__':
    main()
