import pygame
from Class_Computer_Striker import ComputerStriker
from Class_Striker import Striker
from Class_Ball import Ball
from menu import show_winner, display_countdown
from game_setup import font150, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS
pygame.mixer.init()
point_sound = pygame.mixer.Sound("sounds/point.mp3")
point_sound.set_volume(0.5)
def original_mode(game_points, player_vs_computer):
    running = True
    ball_speed = 20
    # Initialize the strikers
    player1_striker = Striker(20, HEIGHT // 2 - 52, 10, 100, 10, GREEN)
    if player_vs_computer:
        player2_striker = ComputerStriker(WIDTH - 30, HEIGHT // 2 - 52, 10, 100, 10, GREEN)
    else:
        player2_striker = Striker(WIDTH - 30, HEIGHT // 2 - 52, 10, 100, 10, GREEN)

    # Initialize the ball with the specified initial velocity
    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, ball_speed, WHITE)

    geek1Score, geek2Score = 0, 0
    player1YFac, player2YFac = 0, 0

    # Display countdown before the game starts
    screen.fill(BLACK)
    display_countdown(3, font150, screen, [player1_striker, player2_striker, ball])

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

        # Check for collision with strikers (without increasing speed)
        if pygame.Rect.colliderect(ball.getRect(), player1_striker.getRect()):
            ball.hit(striker=player1_striker, increase_speed=False)  # No speed increase
        if pygame.Rect.colliderect(ball.getRect(), player2_striker.getRect()):
            ball.hit(striker=player2_striker, increase_speed=False)  # No speed increase

        # Update ball position and check for scoring
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
                display_countdown(3, font150, screen, [player1_striker, player2_striker, ball])
            ball.reset()

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
