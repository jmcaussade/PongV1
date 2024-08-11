import pygame
from game_setup import font20, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS


class Obstacle:
    def __init__(self, posx, posy, width, height, color):
        self.rect = pygame.Rect(posx, posy, width, height)
        self.color = color

    def display(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def getRect(self):
        return self.rect