import sys

import pygame

# Inicialização do Pygame
pygame.init()

# Definições de cores
white = (255, 255, 255)
black = (0, 0, 0)

# Dimensões da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')

# Definindo o relógio
clock = pygame.time.Clock()

# Configurações dos objetos do jogo
paddle_width, paddle_height = 10, 100
ball_size = 20
paddle_speed = 5
ball_speed_x, ball_speed_y = 5, 5

left_paddle = pygame.Rect(
    10, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 20, height // 2 -
                           paddle_height // 2, paddle_width, paddle_height)
ball = pygame.Rect(width // 2 - ball_size // 2, height //
                   2 - ball_size // 2, ball_size, ball_size)


def draw_objects():
    screen.fill(black)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.display.flip()


def move_paddles():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
        right_paddle.y += paddle_speed


def move_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Colisão com o topo e a base
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    # Colisão com as raquetes
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    # Colisão com as bordas
    if ball.left <= 0 or ball.right >= width:
        ball.x = width // 2 - ball_size // 2
        ball.y = height // 2 - ball_size // 2
        ball_speed_x *= -1


def gameLoop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_paddles()
        move_ball()
        draw_objects()
        clock.tick(60)


gameLoop()
