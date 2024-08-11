import pygame
from Class_Striker import Striker
from game_setup import font20, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS


class ComputerStriker(Striker):
    def __init__(self, posx, posy, width, height, speed, color):
        super().__init__(posx, posy, width, height, speed, color)
    
    def update(self, ball):
        # Simple AI to follow the ball
        if self.posy + self.height / 2 < ball.posy:
            self.posy += self.speed
        elif self.posy + self.height / 2 > ball.posy:
            self.posy -= self.speed
        
        # Keep within screen bounds
        if self.posy < 0:
            self.posy = 0
        elif self.posy + self.height > HEIGHT:
            self.posy = HEIGHT - self.height

        self.geekRect = (self.posx, self.posy, self.width, self.height)