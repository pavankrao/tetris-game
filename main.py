import pygame, sys
from grid import Grid

pygame.init()
screen = pygame.display.set_mode((300, 600))
pygame.display.set_caption("Python Tetris")
clock = pygame.time.Clock()

# colors
dark_blue = (44, 44, 127)

game_grid = Grid()

# test grid color fill
# game_grid.grid[0][0] = 1
# game_grid.grid[3][5] = 4
# game_grid.grid[17][8] = 7

game_grid.print_grid()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    # Drawing
    screen.fill(dark_blue)
    game_grid.draw_grid(screen)
    pygame.display.update()
    clock.tick(60)
