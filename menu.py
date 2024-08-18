import pygame
from game_setup import font20, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS

def display_controls_pvp():
    controls_text = [
        "Controls for Player vs Player:",
        "Player 1: Up Arrow / Down Arrow",
        "Player 2: W (Up) / S (Down)",
        "",
        "Press SPACE to Start"
    ]

    screen.fill(BLACK)
    y_offset = 50

    for line in controls_text:
        text_surface = font20.render(line, True, WHITE)
        screen.blit(text_surface, (WIDTH // 4, y_offset))
        y_offset += 30

    pygame.display.update()

def display_controls_pvc():
    controls_text = [
        "Controls for Player vs Computer:",
        "Player 1: Up Arrow / Down Arrow",
        "Computer: Automatically controlled",
        "",
        "Press SPACE to Start"
    ]

    screen.fill(BLACK)
    y_offset = 50

    for line in controls_text:
        text_surface = font20.render(line, True, WHITE)
        screen.blit(text_surface, (WIDTH // 4, y_offset))
        y_offset += 30

    pygame.display.update()

def get_points_limit():
    input_box = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 20, 140, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    font = pygame.font.Font(None, 32)
    txt_surface = font.render('0', True, color)
    active = False
    text = ''
    points_limit = 5  # Default value

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        points_limit = int(text)
                        if 1 <= points_limit <= 20:
                            return points_limit
                        else:
                            text = ''  # Clear text if out of range
                            txt_surface = font.render('Invalid. Enter a number between 1 and 20:', True, color)
                    except ValueError:
                        text = ''  # Clear text on invalid input
                        txt_surface = font.render('Invalid. Enter a number between 1 and 20:', True, color)
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                txt_surface = font.render(text, True, color)
        
        screen.fill(BLACK)

        # Display the prompt message
        prompt_surface = font.render('Enter how many points you want to play (1-20):', True, WHITE)
        screen.blit(prompt_surface, (WIDTH // 2 - prompt_surface.get_width() // 2, HEIGHT // 2 - 100))

        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)
        pygame.display.flip()

        clock.tick(FPS)



def display_menu():
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

def menu():
    while True:
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

        game_choice = None 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
             
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_choice = "increase_speed_pvp"
                elif event.key == pygame.K_2:
                    game_choice = "duplicate_ball_pvp"
                elif event.key == pygame.K_3:
                    game_choice = "obstacle_pvp"
                elif event.key == pygame.K_4:
                    game_choice = "increase_speed_pvc"
                elif event.key == pygame.K_5:
                    game_choice = "duplicate_ball_pvc"
                elif event.key == pygame.K_6:
                    game_choice = "obstacle_pvc"
                
                if game_choice:
                    while True:
                        if "pvp" in game_choice:
                            display_controls_pvp()
                        else:
                            display_controls_pvc()
                        
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                return None
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    points_limit = get_points_limit()
                                    return game_choice, points_limit
                                elif event.key == pygame.K_ESCAPE:
                                    break

        clock.tick(FPS)

