import pygame

from game_setup import WIDTH, HEIGHT, screen


import pygame
import math

class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.initial_speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = True
        self.hit_count = 0

    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
        if self.posx <= 0 and self.firstTime:
            self.firstTime = False
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = False
            return -1
        else:
            return 0

    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = True
        self.speed = self.initial_speed

    def hit(self, striker=None, increase_speed=False, vertical=True):
        if striker:
            # Calculate where the ball hit the striker
            striker_center = striker.posy + striker.height / 2
            impact_point = (self.posy - striker_center) / (striker.height / 2)  # Normalize to range [-1, 1]

            # Adjust the ball's angle based on the impact point
            max_angle = 0.5  # Adjust this value to make the rebound angle more or less steep
            angle_change = impact_point * max_angle

            # Adjust the ball's direction based on the angle
            self.xFac *= -1  # Reverse horizontal direction
            self.yFac = angle_change  # Apply angle change to vertical direction

            if increase_speed:
                self.speed += 1
        else:
            if vertical:
                # Natural rebound logic for vertical obstacles
                self.xFac *= -1  # Reverse horizontal direction
            else:
                # Natural rebound logic for horizontal obstacles
                self.yFac *= -1  # Reverse vertical direction

        self.hit_count += 1

    def getRect(self):
        return pygame.Rect(self.posx - self.radius, self.posy - self.radius, self.radius * 2, self.radius * 2)

