import pygame
from Class_Computer_Striker import ComputerStriker
from Class_Striker import Striker
from Class_Ball import Ball
from Class_Object import Obstacle
from menu import show_winner, display_countdown
import math
from game_setup import font80, font150, BLACK, WHITE, GREEN, PINK, BLUE, WIDTH, HEIGHT, screen, clock, FPS

pygame.mixer.init()
point_sound = pygame.mixer.Sound("sounds/point.mp3")
point_sound.set_volume(0.5)

def obstacle_mode(game_points, player_vs_computer):
    running = True

    # Initialize the strikers
    player1_striker = Striker(20, HEIGHT // 2 - 52, 10, 100, 10, GREEN)
    if player_vs_computer:
        player2_striker = ComputerStriker(WIDTH - 30, HEIGHT // 2 - 52, 10, 100, 10, GREEN)
    else:
        player2_striker = Striker(WIDTH - 30, HEIGHT // 2 - 52, 10, 100, 10, GREEN)

    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 11, WHITE)

    vertical_obstacles = [
        Obstacle(WIDTH // 4, HEIGHT // 4, 20, 100, PINK),
        Obstacle(WIDTH // 2, HEIGHT // 2, 20, 100, PINK),
        Obstacle(WIDTH - (WIDTH // 4), HEIGHT // 4, 20, 100, PINK)
    ]

    horizontal_obstacles = [
        Obstacle(WIDTH // 2.5, HEIGHT - (HEIGHT // 6), 200, 20, BLUE)
    ]
    geek1Score, geek2Score = 0, 0
    player1YFac, player2YFac = 0, 0

    while geek1Score < game_points and geek2Score < game_points:
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
            player2_striker.update([ball])
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
            point_sound.play()
            player1_striker.reset()
            player2_striker.reset()
            if geek1Score < game_points and geek2Score < game_points:
                display_countdown(3, font150, screen, [player1_striker, player2_striker, ball] + vertical_obstacles + horizontal_obstacles)
            ball.reset()
            print(f"Ball reset: xFac={ball.xFac}, yFac={ball.yFac}")

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
    
    show_winner(geek1Score, geek2Score)
    return None
