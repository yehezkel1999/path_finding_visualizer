import pygame
from Grid import Grid
from Node import Node
from AStar import AStar

MOUSE_BUTTONS = 3  # find a way to figure this out
HEIGHT = 600
WIDTH = 800

ROWS = 50


def main():
    window = pygame.display.set_mode((HEIGHT, HEIGHT))  # set up pygame window
    pygame.display.set_caption("Path Finding Visualizer")

    grid = Grid(window, HEIGHT, WIDTH, ROWS)
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

                node.reset()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    algorithm = AStar(grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid.reset()
        if algorithm:
            algorithm.run()
            algorithm = None
        grid.draw()


if __name__ == '__main__':
    main()
