import pygame
from Class_Computer_Striker import ComputerStriker
from Class_Striker import Striker
from Class_Ball import Ball
from menu import show_winner
from game_setup import font20, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS

def duplicate_ball_mode(game_points, player_vs_computer):
    running = True

    # Initialize the strikers
    player1_striker = Striker(20, 200, 10, 100, 10, GREEN)
    if player_vs_computer:
        player2_striker = ComputerStriker(WIDTH - 30, 200, 10, 100, 10, GREEN)
    else:
        player2_striker = Striker(WIDTH - 30, 200, 10, 100, 10, GREEN)

    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    geek1Score, geek2Score = 0, 0
    player1YFac, player2YFac = 0, 0

    balls = [ball]

    while geek1Score < game_points and geek2Score < game_points:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
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

        # Update the players' movements
        player1_striker.update(player1YFac)
        if player_vs_computer:
            player2_striker.update(balls)
        else:
            player2_striker.update(player2YFac)

        # Update the balls
        new_balls = []
        for ball in balls:
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
            if ball.hit_count >= 5:
                ball.hit_count = 0
                new_balls.append(Ball(ball.posx, ball.posy, ball.radius, ball.speed, WHITE))
            new_balls.append(ball)

        balls = new_balls

        # Draw everything
        for ball in balls:
            ball.display()

        player1_striker.display()
        player2_striker.display()

        player1_striker.displayScore("Player 1: ", geek1Score, 100, 20, WHITE)
        if player_vs_computer:
            player2_striker.displayScore("Computer: ", geek2Score, WIDTH - 100, 20, WHITE)
        else:
            player2_striker.displayScore("Player 2: ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)

    show_winner(geek1Score, geek2Score)
    return None
