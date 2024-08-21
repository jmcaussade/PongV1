import pygame
import random

from game_setup import WIDTH, HEIGHT, screen


import pygame
import math


pygame.mixer.init()
class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.initial_speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = 0.01  # Start the ball moving horizontally
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = True
        self.hit_count = 0

        self.hit_sound1 = pygame.mixer.Sound("sounds/hit1.wav")
        self.hit_sound2 = pygame.mixer.Sound("sounds/hit2.wav")

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
        if abs(self.yFac) < 0.02:
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


    def reset(self, increase_speed=False):
        self.posx = WIDTH // 2
        self.posy = HEIGHT // 2
        
        # Set the initial direction to be semi-horizontal
        self.xFac = random.choice([-1, 1])  # Randomly choose direction to start
        self.yFac = random.uniform(0.01, 0.1)  # Semi-horizontal: smaller yFac values for less vertical movement

        self.firstTime = True
        self.hit_count = 0
        if increase_speed:
            self.speed = 7
        else:
            self.speed = self.speed

                

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

            if striker.posx < WIDTH // 2:
                self.hit_sound1.play()  # Sound for the left striker
            else:
                self.hit_sound2.play()  # Sound for the right striker
        self.hit_count += 1


    def handle_vertical_object_collision(self, ball, obstacle):
        # Check collision with the top edge
        if ball.posy - ball.radius < obstacle.rect.top and ball.posy + ball.radius > obstacle.rect.top:
            ball.yFac *= -1  # Reverse vertical direction
            ball.posy = obstacle.rect.top - ball.radius  # Reposition the ball above the obstacle

        # Check collision with the bottom edge
        elif ball.posy + ball.radius > obstacle.rect.bottom and ball.posy - ball.radius < obstacle.rect.bottom:
            ball.yFac *= -1  # Reverse vertical direction
            ball.posy = obstacle.rect.bottom + ball.radius  # Reposition the ball below the obstacle

        # Check collision with the left or right side
        elif ball.posx + ball.radius > obstacle.rect.left and ball.posx - ball.radius < obstacle.rect.left:
            ball.xFac *= -1  # Reverse horizontal direction
            ball.posx = obstacle.rect.left - ball.radius  # Reposition the ball to the left of the obstacle
            ball.posy += 0.1 * ball.yFac  # Slight adjustment to prevent getting stuck

        elif ball.posx - ball.radius < obstacle.rect.right and ball.posx + ball.radius > obstacle.rect.right:
            ball.xFac *= -1  # Reverse horizontal direction
            ball.posx = obstacle.rect.right + ball.radius  # Reposition the ball to the right of the obstacle
            ball.posy += 0.1 * ball.yFac  # Slight adjustment to prevent getting stuck


    def handle_horizontal_object_collision(self, ball, obstacle):
        # Check collision with the left edge
        if ball.posx - ball.radius < obstacle.rect.left and ball.posx + ball.radius > obstacle.rect.left:
            ball.xFac *= -1  # Reverse horizontal direction
            ball.posx = obstacle.rect.left - ball.radius  # Reposition the ball to the left of the obstacle

        # Check collision with the right edge
        elif ball.posx + ball.radius > obstacle.rect.right and ball.posx - ball.radius < obstacle.rect.right:
            ball.xFac *= -1  # Reverse horizontal direction
            ball.posx = obstacle.rect.right + ball.radius  # Reposition the ball to the right of the obstacle

        # Check collision with the top or bottom side
        elif ball.posy - ball.radius < obstacle.rect.top and ball.posy + ball.radius > obstacle.rect.top:
            ball.yFac *= -1  # Reverse vertical direction
            ball.posy = obstacle.rect.top - ball.radius  # Reposition the ball above the obstacle

        elif ball.posy + ball.radius > obstacle.rect.bottom and ball.posy - ball.radius < obstacle.rect.bottom:
            ball.yFac *= -1  # Reverse vertical direction
            ball.posy = obstacle.rect.bottom + ball.radius  # Reposition the ball below the obstacle



    def getRect(self):
        return pygame.Rect(self.posx - self.radius, self.posy - self.radius, self.radius * 2, self.radius * 2)

