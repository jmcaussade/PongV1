import pygame
from game_setup import font20, font40, BLACK, WHITE, GREEN, WIDTH, HEIGHT, screen, clock, FPS

def display_controls_pvp():
    controls_text = [
        "Controls for Player vs Player:",
        "Player 1:  W (Up) / S (Down)",
        "Player 2: Up Arrow / Down Arrow",
        "",
        "Press SPACE to Start",
        "Press ESC to Return to Menu"
    ]

    screen.fill(BLACK)
    y_offset = 50

    for line in controls_text:
        text_surface = font20.render(line, True, WHITE)
        screen.blit(text_surface, (WIDTH // 4, y_offset))
        y_offset += 30

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "pvp" 
                elif event.key == pygame.K_ESCAPE:
                    return "menu"  

def display_controls_pvc():
    controls_text = [
        "Controls for Player vs Computer:",
        "Player 1:  W (Up) / S (Down)",
        "Computer: Automatically controlled",
        "",
        "Press SPACE to Start",
        "Press ESC to Return to Menu"
    ]

    screen.fill(BLACK)
    y_offset = 50

    for line in controls_text:
        text_surface = font20.render(line, True, WHITE)
        screen.blit(text_surface, (WIDTH // 4, y_offset))
        y_offset += 30

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "pvc"
                elif event.key == pygame.K_ESCAPE:
                    return "menu"



def get_points_limit():
    input_box = pygame.Rect(WIDTH // 2 - 70, HEIGHT // 2 + 20, 140, 40)
    color_inactive = pygame.Color('lightskyblue3')
    color = color_inactive
    font = pygame.font.Font(None, 32)
    txt_surface = font.render('1', True, color)
    text = '1'
    points_limit = 1  # Default value

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
                            text = ''  
                            txt_surface = font.render('Invalid. Enter a number between 1 and 20', True, color)
                    except ValueError:
                        text = ''  
                        txt_surface = font.render('Invalid. Enter a number between 1 and 20:', True, color)
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    if event.unicode.isdigit():
                        text += event.unicode
                        # Limit the length of the input to avoid excessive digits
                        if len(text) > 2:
                            text = text[:-1]
                txt_surface = font.render(text, True, color)
        
        screen.fill(BLACK)

        prompt_surface = font.render('Enter how many points you want to play (from 1 to 20):', True, WHITE)
        prompt_rect = prompt_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
        screen.blit(prompt_surface, prompt_rect)
        
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        input_box.center = (WIDTH // 2, HEIGHT // 2 - 40)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(screen, color, input_box, 2)

        instruction_surface = font.render('Press ENTER to confirm', True, WHITE)
        instruction_rect = instruction_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20))
        screen.blit(instruction_surface, instruction_rect)

        pygame.display.flip()

        clock.tick(FPS)



def display_menu():
    screen.fill(BLACK)
    
    # Render title
    title = font40.render("Pong Game", True, WHITE)
    title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4 -50))
    
    # Render instructions
    instructions = font20.render("Press the number key (1-9) to select an option:", True, WHITE)
    instructions_rect = instructions.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 125))
    
    # Render menu options
    option1 = font20.render("1. Increase Speed Mode (Player vs Player)", True, WHITE)
    option1_rect = option1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

    option2 = font20.render("2. Duplicate Ball Mode (Player vs Player)", True, WHITE)
    option2_rect = option2.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 25))

    option3 = font20.render("3. Obstacle Mode (Player vs Player)", True, WHITE)
    option3_rect = option3.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    option4 = font20.render("4. Original Mode (Player vs Player)", True, WHITE)
    option4_rect = option4.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 25))

    option5 = font20.render("5. Increase Speed Mode (Player vs Computer)", True, WHITE)
    option5_rect = option5.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    option6 = font20.render("6. Duplicate Ball Mode (Player vs Computer)", True, WHITE)
    option6_rect = option6.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 75))

    option7 = font20.render("7. Obstacle Mode (Player vs Computer)", True, WHITE)
    option7_rect = option7.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

    option8 = font20.render("8. Original Mode (Player vs Computer)", True, WHITE)
    option8_rect = option8.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 125))

    option9 = font20.render("9. Exit Game", True, WHITE)
    option9_rect = option9.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

    screen.blit(title, title_rect)
    screen.blit(instructions, instructions_rect)
    screen.blit(option1, option1_rect)
    screen.blit(option2, option2_rect)
    screen.blit(option3, option3_rect)
    screen.blit(option4, option4_rect)
    screen.blit(option5, option5_rect)
    screen.blit(option6, option6_rect)
    screen.blit(option7, option7_rect)
    screen.blit(option8, option8_rect)
    screen.blit(option9, option9_rect)

    pygame.display.flip()


def show_winner(points_p1, points_p2):
    screen.fill((0, 0, 0))  # Black background
    if points_p1 > points_p2:
        text = f"Player 1 Wins!"
    else:
        text = f"Player 2 Wins!"
    text_surface = font40.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

    pygame.time.wait(2000)

def menu():
    while True:
        display_menu()

        game_choice = None 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None

            if event.type == pygame.KEYDOWN:
                # pvp = Player VS Player
                # pvc = Player VS Computer
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_choice = "increase_speed_pvp"
                    elif event.key == pygame.K_2:
                        game_choice = "duplicate_ball_pvp"
                    elif event.key == pygame.K_3:
                        game_choice = "obstacle_pvp"
                    elif event.key == pygame.K_4:
                        game_choice = "original_pvp"
                    elif event.key == pygame.K_5:
                        game_choice = "increase_speed_pvc"
                    elif event.key == pygame.K_6:
                        game_choice = "duplicate_ball_pvc"
                    elif event.key == pygame.K_7:
                        game_choice = "obstacle_pvc"
                    elif event.key == pygame.K_8:
                        game_choice = "original_pvc"
                    elif event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        pygame.quit()
                        return None
                
                if game_choice:
                    while True:
                        if "pvp" in game_choice:
                            return_value = display_controls_pvp()
                        else:
                            return_value = display_controls_pvc()
                        
                        if return_value == "menu":
                            break
                        elif return_value in ["pvp", "pvc"]:
                            points_limit = get_points_limit()
                            return game_choice, points_limit

        clock.tick(FPS)
