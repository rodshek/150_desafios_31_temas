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
pygame.display.set_caption('Jogo de Pong')

# Definindo o relógio
clock = pygame.time.Clock()

# Definindo as características da bola e das raquetes
ball_speed = [4, 4]
ball_size = 20
ball = pygame.Rect(width // 2, height // 2, ball_size, ball_size)

paddle_width, paddle_height = 10, 100
paddle_speed = 10
left_paddle = pygame.Rect(
    30, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 30 - paddle_width, height //
                           2 - paddle_height // 2, paddle_width, paddle_height)


def draw_objects():
    screen.fill(black)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.display.flip()


def move_ball():
    global ball_speed
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]
    if ball.left <= 0 or ball.right >= width:
        ball_speed[0] = -ball_speed[0]


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


def check_collisions():
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed[0] = -ball_speed[0]


def gameLoop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        move_ball()
        move_paddles()
        check_collisions()
        draw_objects()
        clock.tick(60)


gameLoop()
