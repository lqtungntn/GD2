import pygame
import os

pygame.font.init()
pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 960, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mini FootBall!!!')
FPS = 60
SCREENID = 0
MODE = 1
SCREEN_RESET = False

