import random

import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da tela
width, height = 300, 600
block_size = 30
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tetris')

# Cores
black = (0, 0, 0)
white = (255, 255, 255)
colors = [
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (0, 255, 0),    # Green
    (255, 255, 0),  # Yellow
    (255, 0, 0),    # Red
    (128, 0, 128),  # Purple
    (0, 0, 255)     # Blue
]

# Definições das formas
shapes = [
    [[1, 1, 1, 1]],         # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1], [1, 1]],       # O
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

# Funções auxiliares


def draw_grid():
    for x in range(0, width, block_size):
        pygame.draw.line(screen, white, (x, 0), (x, height))
    for y in range(0, height, block_size):
        pygame.draw.line(screen, white, (0, y), (width, y))


def draw_shape(shape, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, colors[cell - 1], (offset[0] + x *
                                 block_size, offset[1] + y * block_size, block_size, block_size))


def check_collision(shape, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                px, py = offset[0] + x * block_size, offset[1] + y * block_size
                if px < 0 or px >= width or py >= height:
                    return True
                if py >= 0 and grid[py // block_size][px // block_size]:
                    return True
    return False


def merge_shape(shape, offset):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                grid[offset[1] // block_size +
                     y][offset[0] // block_size + x] = cell


def clear_lines():
    global grid
    new_grid = [row[:] for row in grid]
    new_grid = [row for row in new_grid if any(cell == 0 for cell in row)]
    while len(new_grid) < height // block_size:
        new_grid.insert(0, [0] * (width // block_size))
    grid = new_grid


def game_loop():
    global grid
    clock = pygame.time.Clock()
    shape = random.choice(shapes)
    offset = [width // 2 - len(shape[0]) * block_size // 2, 0]
    grid = [[0] * (width // block_size) for _ in range(height // block_size)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            offset[0] -= block_size
            if check_collision(shape, offset):
                offset[0] += block_size
        if keys[pygame.K_RIGHT]:
            offset[0] += block_size
            if check_collision(shape, offset):
                offset[0] -= block_size
        if keys[pygame.K_DOWN]:
            offset[1] += block_size
            if check_collision(shape, offset):
                offset[1] -= block_size
                merge_shape(shape, offset)
                clear_lines()
                shape = random.choice(shapes)
                offset = [width // 2 - len(shape[0]) * block_size // 2, 0]
                if check_collision(shape, offset):
                    pygame.quit()
                    return
        if keys[pygame.K_UP]:
            shape = [list(row) for row in zip(*shape[::-1])]
            if check_collision(shape, offset):
                shape = [list(row) for row in zip(*shape)][::-1]

        screen.fill(black)
        draw_grid()
        draw_shape(shape, offset)
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen, colors[cell - 1], (x * block_size, y * block_size, block_size, block_size))
        pygame.display.flip()
        clock.tick(10)


game_loop()
