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

def menu():
    running = True
    while running:
        screen.fill(BLACK)
        title = font40.render("Pong Game", True, WHITE)
        title_rect = title.get_rect(center=(WIDTH // 2, HEIGHT // 4))

        option1 = font20.render("1. Increase Speed Mode", True, WHITE)
        option1_rect = option1.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        option2 = font20.render("2. Duplicate Ball Mode", True, WHITE)
        option2_rect = option2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        option3 = font20.render("3. Obstacle Mode", True, WHITE)
        option3_rect = option3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 100))

        screen.blit(title, title_rect)
        screen.blit(option1, option1_rect)
        screen.blit(option2, option2_rect)
        screen.blit(option3, option3_rect)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "increase_speed"
                if event.key == pygame.K_2:
                    return "duplicate_ball"
                if event.key == pygame.K_3:
                    return "obstacle"

        clock.tick(FPS)

    pygame.quit()
    return None

def main():
    while True:
        game_mode = menu()
        if not game_mode:
            break

        if game_mode == "increase_speed":
            increase_speed_mode()
        elif game_mode == "duplicate_ball":
            duplicate_ball_mode()
        elif game_mode == "obstacle":
            obstacle_mode()
        else:
            print("Invalid option")


def increase_speed_mode():
    running = True

    geek1 = Striker(20, 0, 10, 100, 10, GREEN)
    geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    listOfGeeks = [geek1, geek2]

    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit to the main menu
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
                if event.key == pygame.K_w:
                    geek1YFac = -1
                if event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0

        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                ball.hit(increase_speed=True)

        geek1.update(geek1YFac)
        geek2.update(geek2YFac)
        point = ball.update()

        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1

        if point:
            ball.reset()

        geek1.display()
        geek2.display()
        ball.display()

        geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
        geek2.displayScore("Geek_2 : ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

def duplicate_ball_mode():
    running = True

    geek1 = Striker(20, 0, 10, 100, 10, GREEN)
    geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    listOfGeeks = [geek1, geek2]
    balls = [ball]

    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit to the main menu
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
                if event.key == pygame.K_w:
                    geek1YFac = -1
                if event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0

        for geek in listOfGeeks:
            for ball in balls:
                if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                    ball.hit()

        geek1.update(geek1YFac)
        geek2.update(geek2YFac)

        new_balls = []
        for ball in balls:
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

        geek1.display()
        geek2.display()

        geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
        geek2.displayScore("Geek_2 : ", geek2Score, WIDTH - 100, 20, WHITE)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


def obstacle_mode():
    running = True
    
    # Initialize Strikers, Ball, and Obstacles
    geek1 = Striker(20, 0, 10, 100, 10, GREEN)
    geek2 = Striker(WIDTH - 30, 0, 10, 100, 10, GREEN)
    ball = Ball(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)
    
    # Define some obstacles
    obstacles = [
        Obstacle(WIDTH // 4, HEIGHT // 4, 20, 100, WHITE),
        Obstacle(WIDTH // 2, HEIGHT // 2, 20, 100, WHITE)
    ]
    
    listOfGeeks = [geek1, geek2]
    geek1Score, geek2Score = 0, 0
    geek1YFac, geek2YFac = 0, 0

    while running:
        screen.fill(BLACK)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return  # Exit to the main menu
                if event.key == pygame.K_UP:
                    geek2YFac = -1
                if event.key == pygame.K_DOWN:
                    geek2YFac = 1
                if event.key == pygame.K_w:
                    geek1YFac = -1
                if event.key == pygame.K_s:
                    geek1YFac = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    geek2YFac = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    geek1YFac = 0
        
        # Collision detection with obstacles
        for obstacle in obstacles:
            if pygame.Rect.colliderect(ball.getRect(), obstacle.getRect()):
                ball.hit()
        
        # Collision detection with strikers
        for geek in listOfGeeks:
            if pygame.Rect.colliderect(ball.getRect(), geek.getRect()):
                ball.hit()
        
        # Update positions
        geek1.update(geek1YFac)
        geek2.update(geek2YFac)
        point = ball.update()
        
        # Check if a point was scored
        if point == -1:
            geek1Score += 1
        elif point == 1:
            geek2Score += 1
        
        if point:
            ball.reset()
        
        # Display obstacles
        for obstacle in obstacles:
            obstacle.display()
        
        # Display other elements
        geek1.display()
        geek2.display()
        ball.display()
        
        geek1.displayScore("Geek_1 : ", geek1Score, 100, 20, WHITE)
        geek2.displayScore("Geek_2 : ", geek2Score, WIDTH - 100, 20, WHITE)
        
        pygame.display.update()
        clock.tick(FPS)



if __name__ == "__main__":
    main()
