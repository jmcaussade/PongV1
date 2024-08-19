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
        # Update ball position
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac

        # Check for collision with top or bottom border
        if self.posy <= 0:
            self.yFac *= -1
            self.posy = self.radius  # Prevent the ball from going out of bounds
        elif self.posy >= HEIGHT:
            self.yFac *= -1
            self.posy = HEIGHT - self.radius  # Prevent the ball from going out of bounds
        
        # Introduce a small vertical adjustment if the ball is almost moving horizontally
        if abs(self.yFac) < 0.1:
            self.yFac = 0.1 * (1 if self.yFac > 0 else -1)  # Ensure it moves vertically
        
        # Check for scoring
        if self.posx <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.posx >= WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0


    def reset(self):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        self.xFac *= -1
        self.firstTime = True
        self.speed = self.initial_speed

    def hit(self, striker=None, increase_speed=False):
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

        self.hit_count += 1


    def handle_vertical_object_collision(self, ball, obstacle):
        # Check collision with the top edge
        if abs(ball.posy - obstacle.rect.top) < ball.radius:
            ball.yFac *= -1  # Reverse vertical direction
            ball.posy = obstacle.rect.top - ball.radius  # Reposition the ball above the obstacle
        
        # Check collision with the bottom edge
        elif abs(ball.posy - obstacle.rect.bottom) < ball.radius:
            ball.yFac *= -1  # Reverse vertical direction
            ball.posy = obstacle.rect.bottom + ball.radius  # Reposition the ball below the obstacle
        
        # Check collision with the left or right side
        elif abs(ball.posx - obstacle.rect.left) < ball.radius or abs(ball.posx - obstacle.rect.right) < ball.radius:
            ball.xFac *= -1  # Reverse horizontal direction
            
            # Introduce a small vertical adjustment to prevent getting stuck
            adjustment = 0.1 * ball.yFac if ball.yFac != 0 else 0.1  # Small vertical movement
            ball.posy += adjustment
            
            # Reposition the ball to the left or right of the obstacle
            if ball.posx < obstacle.rect.centerx:
                ball.posx = obstacle.rect.left - ball.radius
            else:
                ball.posx = obstacle.rect.right + ball.radius


    def handle_horizontal_object_collision(self, ball, obstacle):
        # Check collision with the left edge
        if abs(ball.posx - obstacle.rect.left) < ball.radius:
            ball.xFac *= -1  # Reverse horizontal direction
            ball.posx = obstacle.rect.left - ball.radius  # Reposition the ball to the left of the obstacle
        # Check collision with the right edge
        elif abs(ball.posx - obstacle.rect.right) < ball.radius:
            ball.xFac *= -1  # Reverse horizontal direction
            ball.posx = obstacle.rect.right + ball.radius  # Reposition the ball to the right of the obstacle
        # Check collision with the top or bottom side
        elif abs(ball.posy - obstacle.rect.top) < ball.radius or abs(ball.posy - obstacle.rect.bottom) < ball.radius:
            ball.yFac *= -1  # Reverse vertical direction
            # Reposition the ball above or below the obstacle
            if ball.posy < obstacle.rect.centery:
                ball.posy = obstacle.rect.top - ball.radius
            else:
                ball.posy = obstacle.rect.bottom + ball.radius


    def getRect(self):
        return pygame.Rect(self.posx - self.radius, self.posy - self.radius, self.radius * 2, self.radius * 2)

