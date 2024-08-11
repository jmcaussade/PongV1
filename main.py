import pygame

pygame.init()

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)
font40 = pygame.font.Font('freesansbold.ttf', 40)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

clock = pygame.time.Clock()
FPS = 30

class Striker:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.geekRect = pygame.Rect(posx, posy, width, height)
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def display(self):
        self.geek = pygame.draw.rect(screen, self.color, self.geekRect)

    def update(self, yFac):
        self.posy = self.posy + self.speed * yFac
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height
        self.geekRect = (self.posx, self.posy, self.width, self.height)

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        screen.blit(text, textRect)

    def getRect(self):
        return self.geekRect

class Ball:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.initial_speed = speed  # Store the initial speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)
        self.firstTime = 1
        self.hit_count = 0

    def display(self):
        self.ball = pygame.draw.circle(screen, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed * self.xFac
        self.posy += self.speed * self.yFac
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
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
        self.firstTime = 1
        self.speed = self.initial_speed  # Reset speed to initial value

    def hit(self, increase_speed=False):
        self.xFac *= -1
        if increase_speed:
            self.speed += 1
        self.hit_count += 1

    def getRect(self):
        return self.ball

class Obstacle:
    def __init__(self, posx, posy, width, height, color):
        self.rect = pygame.Rect(posx, posy, width, height)
        self.color = color

    def display(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def getRect(self):
        return self.rect

class ComputerStriker(Striker):
    def __init__(self, posx, posy, width, height, speed, color):
        super().__init__(posx, posy, width, height, speed, color)
    
    def update(self, ball):
        # Simple AI to follow the ball
        if self.posy + self.height / 2 < ball.posy:
            self.posy += self.speed
        elif self.posy + self.height / 2 > ball.posy:
            self.posy -= self.speed
        
        # Keep within screen bounds
        if self.posy < 0:
            self.posy = 0
        elif self.posy + self.height > HEIGHT:
            self.posy = HEIGHT - self.height

        self.geekRect = (self.posx, self.posy, self.width, self.height)


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


def main():
    while True:
        game_mode = menu()
        if not game_mode:
            break

        if game_mode == "increase_speed_pvp":
            increase_speed_mode(player_vs_computer=False)
        elif game_mode == "increase_speed_pvc":
            increase_speed_mode(player_vs_computer=True)
        elif game_mode == "duplicate_ball_pvp":
            duplicate_ball_mode(player_vs_computer=False)
        elif game_mode == "duplicate_ball_pvc":
            duplicate_ball_mode(player_vs_computer=True)
        elif game_mode == "obstacle_pvp":
            obstacle_mode(player_vs_computer=False)
        elif game_mode == "obstacle_pvc":
            obstacle_mode(player_vs_computer=True)
        else:
            print("Invalid option")


def increase_speed_mode(player_vs_computer):
    running = True

    player_striker = Striker(20, 0, 10, 100, 10, GREEN)
    if player_vs_computer:
        computer_striker = ComputerStriker(WIDTH - 30, 0, 10, 100, 10, GREEN)
        listOfGeeks = [player_striker, computer_striker]
    else:
        computer_striker = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
        listOfGeeks = [player_striker, computer_striker]

    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    geek1Score, geek2Score = 0, 0
    playerYFac = 0

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit to the main menu
                if event.key == pygame.K_UP:
                    playerYFac = -1
                if event.key == pygame.K_DOWN:
                    playerYFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerYFac = 0

        player_striker.update(playerYFac)
        if player_vs_computer:
            computer_striker.update(ball)
        else:
            computer_striker.update(playerYFac)
        
        for striker in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), striker.getRect()):
                ball.hit(increase_speed=True)

        point = ball.update()

        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1

        if point:
            ball.reset()

        player_striker.display()
        if player_vs_computer:
            computer_striker.display()
        else:
            computer_striker.display()
        ball.display()

        player_striker.displayScore("Player: ", geek1Score, 100, 20, WHITE)
        if player_vs_computer:
            computer_striker.displayScore("Computer: ", geek2Score, WIDTH - 100, 20, WHITE)
        else:
            computer_striker.displayScore("Player 2: ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

def duplicate_ball_mode(player_vs_computer):
    running = True

    player_striker = Striker(20, 0, 10, 100, 10, GREEN)
    if player_vs_computer:
        computer_striker = ComputerStriker(WIDTH - 30, 0, 10, 100, 10, GREEN)
        listOfGeeks = [player_striker, computer_striker]
    else:
        computer_striker = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
        listOfGeeks = [player_striker, computer_striker]

    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    geek1Score, geek2Score = 0, 0
    playerYFac = 0

    balls = [ball]

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit to the main menu
                if event.key == pygame.K_UP:
                    playerYFac = -1
                if event.key == pygame.K_DOWN:
                    playerYFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerYFac = 0

        player_striker.update(playerYFac)
        if player_vs_computer:
            computer_striker.update(ball)
        else:
            computer_striker.update(playerYFac)

        new_balls = []
        for ball in balls:
            if pygame.Rect.colliderect(ball.getRect(), player_striker.getRect()) or pygame.Rect.colliderect(ball.getRect(), computer_striker.getRect()):
                ball.hit()

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

        for ball in balls:
            ball.display()

        player_striker.display()
        if player_vs_computer:
            computer_striker.display()
        else:
            computer_striker.display()

        player_striker.displayScore("Player: ", geek1Score, 100, 20, WHITE)
        if player_vs_computer:
            computer_striker.displayScore("Computer: ", geek2Score, WIDTH - 100, 20, WHITE)
        else:
            computer_striker.displayScore("Player 2: ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


def obstacle_mode(player_vs_computer):
    running = True

    player_striker = Striker(20, 0, 10, 100, 10, GREEN)
    if player_vs_computer:
        computer_striker = ComputerStriker(WIDTH - 30, 0, 10, 100, 10, GREEN)
        listOfGeeks = [player_striker, computer_striker]
    else:
        computer_striker = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
        listOfGeeks = [player_striker, computer_striker]

    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    obstacles = [
        Obstacle(WIDTH // 4, HEIGHT // 4, 20, 100, WHITE),
        Obstacle(WIDTH // 2, HEIGHT // 2, 20, 100, WHITE)
    ]

    geek1Score, geek2Score = 0, 0
    playerYFac = 0

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit to the main menu
                if event.key == pygame.K_UP:
                    playerYFac = -1
                if event.key == pygame.K_DOWN:
                    playerYFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerYFac = 0

        player_striker.update(playerYFac)
        if player_vs_computer:
            computer_striker.update(ball)
        else:
            computer_striker.update(playerYFac)

        for obstacle in obstacles:
            if pygame.Rect.colliderect(ball.getRect(), obstacle.getRect()):
                ball.hit()

        for striker in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), striker.getRect()):
                ball.hit()

        point = ball.update()
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1
        if point:
            ball.reset()

        for obstacle in obstacles:
            obstacle.display()

        player_striker.display()
        if player_vs_computer:
            computer_striker.display()
        else:
            computer_striker.display()
        ball.display()

        player_striker.displayScore("Player: ", geek1Score, 100, 20, WHITE)
        if player_vs_computer:
            computer_striker.displayScore("Computer: ", geek2Score, WIDTH - 100, 20, WHITE)
        else:
            computer_striker.displayScore("Player 2: ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()




if __name__ == "__main__":
    main()
