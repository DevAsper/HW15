import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set.mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игровой Тир")
icon = pygame.image.load("img/shoot_game_logo.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.radint(0, SCREEN_WIDTH - target_width)
target_y = random.radint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass

pygame.quit()



