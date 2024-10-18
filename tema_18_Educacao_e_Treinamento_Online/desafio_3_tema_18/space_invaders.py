import random
import sys

import pygame

# Inicialização do Pygame
pygame.init()

# Definições de cores
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Dimensões da tela
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space Invaders')

# Definindo o relógio
clock = pygame.time.Clock()

# Configurações dos objetos do jogo
player_width, player_height = 60, 20
player = pygame.Rect(width // 2 - player_width // 2,
                     height - player_height - 10, player_width, player_height)
player_speed = 5

bullet_width, bullet_height = 5, 10
bullet_speed = 7
bullets = []

enemy_width, enemy_height = 40, 30
enemy_speed = 3
enemies = [pygame.Rect(random.randint(0, width - enemy_width), random.randint(-100,
                       height - enemy_height), enemy_width, enemy_height) for _ in range(10)]


def draw_objects():
    screen.fill(black)
    pygame.draw.rect(screen, green, player)
    for bullet in bullets:
        pygame.draw.rect(screen, white, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, green, enemy)
    pygame.display.flip()


def move_player():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < width:
        player.x += player_speed


def shoot_bullet():
    if len(bullets) < 5:
        bullet = pygame.Rect(player.centerx - bullet_width // 2,
                             player.top - bullet_height, bullet_width, bullet_height)
        bullets.append(bullet)


def move_bullets():
    global bullets
    bullets = [b.move(0, -bullet_speed) for b in bullets if b.bottom > 0]


def move_enemies():
    global enemies
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.top > height:
            enemy.x = random.randint(0, width - enemy_width)
            enemy.y = random.randint(-100, -enemy_height)


def check_collisions():
    global bullets, enemies
    for bullet in bullets:
        for enemy in enemies:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                enemies.append(pygame.Rect(random.randint(0, width - enemy_width),
                               random.randint(-100, height - enemy_height), enemy_width, enemy_height))
                break
    for enemy in enemies:
        if enemy.colliderect(player):
            pygame.quit()
            sys.exit()


def gameLoop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    shoot_bullet()

        move_player()
        move_bullets()
        move_enemies()
        check_collisions()
        draw_objects()
        clock.tick(60)


gameLoop()
