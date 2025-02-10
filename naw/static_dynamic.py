import pygame
import time
import random

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
game_font = pygame.font.SysFont('Arial', 20)
text_display_coords = (20, 600)

# setting background
default_image_size = (720, 720)
bg_image = "background.png"
imp = pygame.image.load(bg_image).convert()
imp = pygame.transform.scale(imp, default_image_size)

# Draw background and static elements once
screen.blit(imp, (0, 0))

# image management
# v penguin
v_penguin = pygame.image.load('v_penguin.png').convert_alpha()
v_ducking = pygame.image.load('v_ducking.png').convert_alpha()
v_ducking = pygame.transform.scale(v_ducking, (200, 200))
v_penguin = pygame.transform.scale(v_penguin, (250, 250))
v_penguin_rect = v_penguin.get_rect()
v_penguin_rect.x = 400
v_penguin_rect.y = 500
screen.blit(v_penguin, v_penguin_rect)

# penguin me
a_penguin = pygame.image.load('a_penguin.png').convert_alpha()
a_penguin = pygame.transform.scale(a_penguin, (70, 70))
a_penguin_rect = a_penguin.get_rect()
a_penguin_rect.x = 650
a_penguin_rect.y = 310
screen.blit(a_penguin, a_penguin_rect)

# hugging penguin
hugging_penguins = pygame.image.load('hugging_penguins.png').convert_alpha()
hugging_penguins = pygame.transform.scale(hugging_penguins, (110, 70))

# hearts
heart_open = pygame.image.load('heart_open.png').convert_alpha()
heart_open = pygame.transform.scale(heart_open, (110, 110))

heart_closed = pygame.image.load('heart_closed.png').convert_alpha()
heart_closed = pygame.transform.scale(heart_closed, (85, 85))

# Update display after drawing static elements
pygame.display.flip()

# function to print the hearts and maybe kill em
class love_bomb(pygame.sprite.Sprite):
    def __init__(self, position_x):
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.health = 2
        self.speed = 10
        self.open_or_closed = 0
        self.sprites = [heart_closed, heart_open]
        self.image = self.sprites[self.open_or_closed]
        self.rect = self.image.get_rect()
        self.rect.x = self.position_x
        self.rect.y = 0  # Initialize the rect's y position

    def update(self):
        global no_of_lives, kills_to_win
        self.rect.move_ip(0, self.speed)
        if self.rect.y >= 500:
            self.kill()
            # no_of_lives -= 1
        
        if self.health == 0:
            self.kill()
            kills_to_win -= 1

        if self.open_or_closed == 0:
            self.image = self.sprites[self.open_or_closed]
            self.open_or_closed = 1
        else:
            self.image = self.sprites[self.open_or_closed]
            self.open_or_closed = 0
    
    def set_speed(self, speed):
        self.speed = speed
        
    def set_health(self, health):
        self.health = health

def display_compliments():
    compliments = [
        "dang you're doing so well keep going hottie ;)",
        "Those gym sessions be paying offf",
        "awesome <3 wish I could kiss thy face off",
        "You can do this, I'll meet you eventually :(",
        "smack them monsters as hard as I'd smack that ass.",
        "That jawline alone could cut through em.",
        "jesus pick me up already",
        "who knew this cutie patootie is that good at murder",
        "imagine they're buncha tiny kids!",
        "Do it for Pedokotaa *moans*",
        "Mind giving be a little twirl while you're at it?",
        "do it like the good girl you are ;)",
        "Make them scream louder than the kids in your basement"
    ]
    compliment_no = random.randint(0, len(compliments) - 1)
    display1 = game_font.render(compliments[compliment_no], True, (255, 220, 255))
    screen.blit(display1, text_display_coords)

def start():
    display1 = game_font.render("Think You Handle Me??", True, (255, 220, 255)) 
    display2 = game_font.render("Meet me (eventually) if you can <3", True, (255, 220, 255)) 
    screen.blit(display1, text_display_coords)
    screen.blit(display2, (20, 620))
    pygame.display.flip()

def end_sequence(did_you_win):
    if did_you_win:
        display = game_font.render("Awesome, you did it <3", True, (255, 220, 255))
        screen.blit(display, text_display_coords)
        pygame.display.flip()
        screen.blit(hugging_penguins, v_penguin_rect)
        pygame.display.flip()
    else:
        display = game_font.render("How unfortunate, I'm afraid I'll have to leave now", True, (255, 220, 255))
        screen.blit(display, text_display_coords)
        pygame.display.flip()
        a_penguin_rect.x = 1000
        screen.blit(v_ducking, v_penguin_rect)

# random game variables
no_of_lives = 3
kill_count = 0
kills_to_win = random.randint(10, 20)
did_you_win = False
love_bombs = pygame.sprite.Group()

waiting = True

while running:
    while waiting:
        if did_you_win:
            end_sequence(did_you_win)
            start()
        else:
            start()
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False

            if event.type == pygame.QUIT:
                waiting = False
                running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            
    generate_heart_odds = random.randint(0, 30)
    if generate_heart_odds == 0:
        love_bomb_1 = love_bomb(random.randint(50, 500))
        love_bombs.add(love_bomb_1)

    # Clear the screen without redrawing the background
    screen.blit(imp, (0, 0))  # This keeps the compliments visible
    love_bombs.update()       # Update the positions of the love bombs
    love_bombs.draw(screen)   # Draw the love bombs

    # Display compliments
    display_compliments()

    pygame.display.flip()

    if no_of_lives == 0:
        did_you_win = False
        end_sequence(did_you_win)
        running = False
    if kills_to_win == 0:
        did_you_win = True
        end_sequence(did_you_win)
        running = False

    clock.tick(20)  # Limits FPS to 20
    pygame.display.set_caption('miss me? ;)')

pygame.quit()
