import pygame
from Class_Computer_Striker import ComputerStriker
from Class_Striker import Striker
from Class_Ball import Ball
from Class_Object import Obstacle
import math
from game_setup import font20, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS

def calculate_normal(ball_rect, object_rect):
    # Calculate the normal vector for natural rebound off obstacles
    ball_center = (ball_rect.centerx, ball_rect.centery)
    object_center = (object_rect.centerx, object_rect.centery)
    normal = (ball_center[0] - object_center[0], ball_center[1] - object_center[1])
    length = math.sqrt(normal[0]**2 + normal[1]**2)
    normal = (normal[0] / length, normal[1] / length)
    return normal

def obstacle_mode(game_points, player_vs_computer):
    running = True

    # Initialize the strikers
    player1_striker = Striker(20, 200, 10, 100, 10, GREEN)
    if player_vs_computer:
        player2_striker = ComputerStriker(WIDTH - 30, 200, 10, 100, 10, GREEN)
    else:
        player2_striker = Striker(WIDTH - 30, 200, 10, 100, 10, GREEN)

    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 12, WHITE)

    vertical_obstacles = [
        Obstacle(WIDTH // 4, HEIGHT // 4, 20, 100, WHITE),
        Obstacle(WIDTH // 2, HEIGHT // 2, 20, 100, WHITE),
        Obstacle(WIDTH - (WIDTH // 4), HEIGHT // 4, 20, 100, WHITE)
    ]

    horizontal_obstacles = [
        Obstacle(WIDTH // 2.5, HEIGHT - (HEIGHT // 6), 200, 20, WHITE)
    ]
    geek1Score, geek2Score = 0, 0
    player1YFac, player2YFac = 0, 0

    while geek1Score <= game_points and geek2Score <= game_points:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit to the main menu
                if event.key == pygame.K_UP:
                    player2YFac = -1
                if event.key == pygame.K_DOWN:
                    player2YFac = 1
                if event.key == pygame.K_w:
                    player1YFac = -1
                if event.key == pygame.K_s:
                    player1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1YFac = 0

        # Update the strikers
        player1_striker.update(player1YFac)
        if player_vs_computer:
            player2_striker.update(ball)
        else:
            player2_striker.update(player2YFac)

        # Update the ball for vertical objects
        for obstacle in vertical_obstacles:
            if pygame.Rect.colliderect(ball.getRect(), obstacle.getRect()):
                ball.handle_vertical_object_collision(ball, obstacle)

        # Update the ball for horizontal objects
        for obstacle in horizontal_obstacles:
            if pygame.Rect.colliderect(ball.getRect(), obstacle.getRect()):
                ball.handle_horizontal_object_collision(ball, obstacle)

        # Check for collision with player1's striker
        if pygame.Rect.colliderect(ball.getRect(), player1_striker.getRect()):
            ball.hit(striker=player1_striker, increase_speed=False)
        if pygame.Rect.colliderect(ball.getRect(), player2_striker.getRect()):
            ball.hit(striker=player2_striker, increase_speed=False)

        point = ball.update()
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1
        if point:
            ball.reset()

        # Draw everything
        for obstacle in vertical_obstacles:
            obstacle.display()

        for obstacle in horizontal_obstacles:
            obstacle.display()

        player1_striker.display()
        player2_striker.display()
        ball.display()

        player1_striker.displayScore("Player 1: ", geek1Score, 100, 20, WHITE)
        if player_vs_computer:
            player2_striker.displayScore("Computer: ", geek2Score, WIDTH - 100, 20, WHITE)
        else:
            player2_striker.displayScore("Player 2: ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)

    return None
