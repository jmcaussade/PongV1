import pygame
from Class_Striker import Striker
from game_setup import WIDTH, HEIGHT

class ComputerStriker(Striker):
    def __init__(self, posx, posy, width, height, speed, color):
        super().__init__(posx, posy, width, height, speed, color)
    
    def update(self, balls):
        # Find the closest ball
        closest_ball = None
        min_distance = float('inf')

        for ball in balls:
            distance = abs(ball.posy - self.posy - self.height / 2)
            if distance < min_distance:
                min_distance = distance
                closest_ball = ball
        
        if closest_ball:
            # Calculate the target position
            target_y = closest_ball.posy - self.height / 2
            
            # Smoothly move the paddle towards the target position
            self.posy += (target_y - self.posy) * 0.1  # Adjust the factor for smoothness
            
            # Keep within screen bounds
            if self.posy < 0:
                self.posy = 0
            elif self.posy + self.height > HEIGHT:
                self.posy = HEIGHT - self.height
        
        self.geekRect = pygame.Rect(self.posx, self.posy, self.width, self.height)
