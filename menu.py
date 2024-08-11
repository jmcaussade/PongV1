import pygame 

from game_setup import font20, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS

def menu():
    running = True
    while running:
        screen.fill(BLACK)
        title = font40.render("Pong Game", True, WHITE)
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        option1 = font20.render("1. Increase Speed Mode (Player vs Player)", True, WHITE)
        option1_rect = option1.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        option2 = font20.render("2. Duplicate Ball Mode (Player vs Player)", True, WHITE)
        option2_rect = option2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        option3 = font20.render("3. Obstacle Mode (Player vs Player)", True, WHITE)
        option3_rect = option3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        option4 = font20.render("4. Increase Speed Mode (Player vs Computer)", True, WHITE)
        option4_rect = option4.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

        option5 = font20.render("5. Duplicate Ball Mode (Player vs Computer)", True, WHITE)
        option5_rect = option5.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 200))

        option6 = font20.render("6. Obstacle Mode (Player vs Computer)", True, WHITE)
        option6_rect = option6.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 250))

        screen.blit(title, title_rect)
        screen.blit(option1, option1_rect)
        screen.blit(option2, option2_rect)
        screen.blit(option3, option3_rect)
        screen.blit(option4, option4_rect)
        screen.blit(option5, option5_rect)
        screen.blit(option6, option6_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "increase_speed_pvp"
                if event.key == pygame.K_2:
                    return "duplicate_ball_pvp"
                if event.key == pygame.K_3:
                    return "obstacle_pvp"
                if event.key == pygame.K_4:
                    return "increase_speed_pvc"
                if event.key == pygame.K_5:
                    return "duplicate_ball_pvc"
                if event.key == pygame.K_6:
                    return "obstacle_pvc"

        clock.tick(FPS)

    pygame.quit()
    return None