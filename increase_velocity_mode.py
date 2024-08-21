import pygame
from Class_Computer_Striker import ComputerStriker
from Class_Striker import Striker
from Class_Ball import Ball
from game_setup import font20, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS
from menu import show_winner

def increase_speed_mode(game_points, player_vs_computer):
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
            player2_striker.update([ball])
        else:
            player2_striker.update(player2YFac)

        # Check for collision with strikers
        if pygame.Rect.colliderect(ball.getRect(), player1_striker.getRect()):
            ball.hit(striker=player1_striker, increase_speed=True)
        if pygame.Rect.colliderect(ball.getRect(), player2_striker.getRect()):
            ball.hit(striker=player2_striker, increase_speed=True)

        # Update ball position and check for scoring
        point = ball.update()
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1
        if point:
            ball.reset(increase_speed=True)
            player1_striker.reset()
            player2_striker.reset()

        # Display everything on the screen
        player1_striker.display()
        player2_striker.display()
        ball.display()

        # Display scores
        player1_striker.displayScore("Player 1: ", geek1Score, 100, 20, WHITE)
        player2_striker.displayScore("Player 2: ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)


    show_winner(geek1Score, geek2Score)
    return None
