import pygame
import random
import time

# Date to check if anniversary
current_time = time.time()
local_time = time.localtime(current_time)
month_string = time.strftime('%d', local_time)


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True

#font
big_game_font = pygame.font.Font('Pacifico.ttf', 36)
center_display_coords = (80, 300)
game_font = pygame.font.Font('Pacifico.ttf', 20)
text_display_coords = (20, 640)

# Load and set background
default_image_size = (720, 720)
bg_image = "background.png"
imp = pygame.image.load(bg_image).convert()
imp = pygame.transform.scale(imp, default_image_size)
screen.blit(imp, (0, 0))
pygame.display.flip()

# Image management
# Penguin images
v_penguin = pygame.image.load('v_penguin.png').convert_alpha()
v_penguin = pygame.transform.scale(v_penguin, (250, 250))
v_penguin_rect = v_penguin.get_rect()
v_penguin_rect.x = 400
v_penguin_rect.y = 500

v_ducking = pygame.image.load('v_ducking.png').convert_alpha()
v_ducking = pygame.transform.scale(v_ducking, (200, 200))


# Player penguin images
a_penguin = pygame.image.load('a_penguin.png').convert_alpha()
a_penguin = pygame.transform.scale(a_penguin, (70, 70))
a_penguin_rect = a_penguin.get_rect()
a_penguin_rect.x = 650
a_penguin_rect.y = 310

a_penguin_big = pygame.image.load('a_penguin.png').convert_alpha()
a_penguin_big = pygame.transform.scale(a_penguin_big, (150, 150))
a_penguin_big_rect = a_penguin_big.get_rect()
a_penguin_big_rect.x = 720
a_penguin_big_rect.y = 550

# Hugging penguins image
hugging_penguins = pygame.image.load('hugging_penguins.png').convert_alpha()
hugging_penguins = pygame.transform.scale(hugging_penguins, (240, 240))

# Heart images
heart_open = pygame.image.load('heart_open.png').convert_alpha()
heart_open = pygame.transform.scale(heart_open, (110, 110))

heart_2 = pygame.image.load('heart_2.png').convert_alpha()
heart_2 = pygame.transform.scale(heart_2, (110, 110))

heart_3 = pygame.image.load('heart_3.png').convert_alpha()
heart_3 = pygame.transform.scale(heart_3, (110, 110))

heart_closed = pygame.image.load('heart_closed.png').convert_alpha()
heart_closed = pygame.transform.scale(heart_closed, (110, 110))

#scene2 helper functions
a_penguin_came_to_you = False
a_penguin_is_far_away = True
jk_id_never=False

def cause_i_cant_fix_bug(scenario):
    """
    Handles various game scenarios by updating the screen
    and drawing necessary elements.
    """
    global a_penguin_is_far_away, a_penguin_came_to_you, a_penguin_rect, jk_id_never
    # Start screen
    if scenario == 0:
        screen.blit(imp, (0, 0))
    
    # In-game
    elif scenario == 1:  
        screen.blit(imp, (0, 0))
        display = big_game_font.render(str(no_of_lives), True, (255, 220, 255))
        screen.blit(display, (655, 285))
        screen.blit(v_penguin, v_penguin_rect)
        screen.blit(a_penguin, a_penguin_rect)
        
    # Player wins
    elif scenario == 2:  
        #explaination: small penguin leaves screen then big penguin comes and turns into hug
        screen.blit(imp, (0, 0))
        if a_penguin_is_far_away:
            a_penguin_rect.x += 3
            screen.blit(a_penguin, a_penguin_rect)
        if a_penguin_rect.x > 720:
            a_penguin_is_far_away = False
        if not a_penguin_is_far_away and not a_penguin_came_to_you:
            a_penguin_big_rect.x -= 4
            screen.blit(a_penguin_big, a_penguin_big_rect)
        if not a_penguin_came_to_you:
            screen.blit(v_penguin, v_penguin_rect)
        if a_penguin_big_rect.x < (v_penguin_rect.x):
            a_penguin_came_to_you = True
            screen.blit(hugging_penguins, v_penguin_rect)
        display = big_game_font.render("Awesome, you did it <3", True, (255, 220, 255))
        screen.blit(display, (200, 350))
        
    # Player loses
    elif scenario == 3:  
        screen.blit(imp, (0, 0))
        screen.blit(a_penguin, a_penguin_rect)
        display1 = big_game_font.render("How unfortunate, I'm afraid I'll have to leave now", True, (255, 220, 255))
        display2 = big_game_font.render("JK, I'd never.", True, (255, 220, 255))
        if jk_id_never is False:
            screen.blit(display1, (0, 350))
            screen.blit(v_ducking, v_penguin_rect)
            a_penguin_rect.x += 1
            if a_penguin_rect.x >= 715:
                jk_id_never=True   
        else: #if jk_id_never is true
            screen.blit(display2, (250, 350))
            if a_penguin_rect.x>=640:
                a_penguin_rect.x -= 2
                screen.blit(v_ducking, v_penguin_rect)
            else:
                screen.blit(v_penguin, v_penguin_rect)
            

# Love bomb class
class love_bomb(pygame.sprite.Sprite):
    """
    Class to handle love bomb sprites, including movement,
    animation, and collision detection.
    """
    def __init__(self, position_x):
        pygame.sprite.Sprite.__init__(self)
        self.position_x = position_x
        self.health = 2
        self.speed = 13

        # Attributes for animation
        self.sprites = [heart_open, heart_2, heart_3, heart_2, heart_open, heart_open]
        self.current_sprite = random.randint(0, len(self.sprites) - 1)
        self.image = self.sprites[int(self.current_sprite)]
        self.animation_speed = 0.20
        self.current_sprite = 0

        # Getting image rect
        self.rect = self.image.get_rect()
        self.rect.center = (self.position_x, 0)
        self.rect.y = 0  # Initialize the rect's y position

        # Double hearts feature
        self.double_hearts_odd = random.randint(0, 10)
        self.double = True if self.double_hearts_odd == 0 else False
        self.double_y = random.randint(200, 350)
        self.double_it_rn = False

    def create(self):
        screen.blit(self.image, self.rect)

    def kill_love_bomb(self):
        self.kill()

    def update(self):
        global no_of_lives, kills_to_win
        self.rect.y += self.speed
        if self.rect.y >= 500:
            self.kill()
            no_of_lives -= 1
        if self.health == 0:
            self.kill()
            kills_to_win -= 1

        # Animation code
        self.current_sprite += self.animation_speed
        if int(self.current_sprite) >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

        screen.blit(self.image, self.rect)

    # Functions for period mode
    def set_speed(self, speed):
        self.speed = speed

    def set_health(self, health):
        self.health = health

    # Functions for double hearts
    def set_y_position(self, y_position):
        self.rect.y = y_position

    def get_y_position(self):
        return self.rect.y

    def double_it(self):
        self.double_it_rn = True

    def decrease_health(self):
        self.health -= 1

def kill_all_love_bombs(love_bombs):
    """
    Kills all active love bombs.
    """
    for love_bomb in love_bombs:
        love_bomb.kill()

def collision_detection(mouse_position, love_bombs):
    """
    Detects collision between mouse position and love bombs.
    """
    for love_bomb in love_bombs:
        if love_bomb.rect.collidepoint(mouse_position):
            love_bomb.decrease_health()

# Compliments list
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
    "Mind giving me a little twirl while you're at it?",
    "do it like the good girl you are ;)",
    "Make em scream louder than the kids in your basement",
    "Jesus, I like you and I miss you. Why am i not with you?",
    "Also, yes these random compliments just be there to distract",
    "Don't fuck up or I'll have to give you back your jackets :(",
    "Too easy for ya huh? Dw, I'll make an update and 10x harder",
    "I think my sister's starting to get jealous of you :(",
    "This game was way harder than it looked :cries:",
    "Glad I made this for you, you're worth it.",
    "Ay, nail them academics as hard as you'd nail me",
    "Guys, look who I pulledd",
    "I'll (maybe) let my toushie be yours",
    "I'm gonna peg you. Rough and fast",
    "Vatsank... ",
    "I'll try to do everything to treat you the way you deserve",
    "Maybe we can do LDR? I'd hope so...",
    "I swear, If I lose you... that'd be the biggest mistake I make",
    "How are you so precious?",
    "Wish you could see yourself from my eyes, you'd be in love fr",
    "no lube, no protection, all night, all day, from the kitchen...",
    "Imma watch you sleep all night (your snoring be music)",
    "Kidnap me. I'd be a new addition to your basement",
    "You make my heart flutter out of my body",
    "You are a risk to my life. Give me heart attacks (good way)",
    "I might (lowkey) be a bottom for ya",
    "abcdefghijklmnopqrstuvuvuv UvU ~anoothi(im being ironic)",
]

class DisplayCompliments:
    def __init__(self):
        self.compliment_no = random.randint(0, len(compliments) - 1)
        self.display_time = 0
        self.display1 = game_font.render(compliments[self.compliment_no], True, (255, 220, 255))
        
    def show(self):
        if generate_hearts_rn:
            if self.display_time > 0:
                screen.blit(self.display1, text_display_coords)
                self.display_time -= 1
            
    def start_display(self):
        self.compliment_no = random.randint(0, len(compliments) - 1)
        self.display1 = game_font.render(compliments[self.compliment_no], True, (255, 220, 255))
        self.display_time = 200  # Set the display time to 200 frames

def start():
    display_anniversary=big_game_font.render("Happy Anniversary!", True, (255, 220, 255)) 
    display1 = big_game_font.render("Think you can handle my love??", True, (255, 220, 255)) 
    display2 = big_game_font.render("Meet me (eventually) if you can <3", True, (255, 220, 255))
    screen.blit(display1, (90, 300))
    screen.blit(display2, (80, 350))
    
    if month_string=="12": 
        screen.blit(display_anniversary, (170, 240))
    if period_mode:
        display3 = big_game_font.render("Period Mode", True, (255, 220, 255)) 
        screen.blit(display3, (210, 410))
    pygame.display.flip()
    
'''
#incase you want to make a gamestates manager
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
'''

# random game variables
no_of_lives = 3
kill_count = 0
kills_to_win = random.randint(10, 30)
kills_to_win = 1
did_you_win = False
love_bombs = pygame.sprite.Group()
generate_hearts_rn = True
period_mode=False

period_mode_odds=random.randint(0, 6)
if period_mode_odds==0:
    period_mode=True
   
    
compliment_display = DisplayCompliments()



waiting = True

while running:
    while waiting:
        if did_you_win:
            start()
            cause_i_cant_fix_bug(0)
        else:
            start()
            cause_i_cant_fix_bug(0)
            
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
            collision_detection(mouse_position, love_bombs)
            
    if generate_hearts_rn: 
        cause_i_cant_fix_bug(1)               
        generate_heart_odds = random.randint(0, 28)
        if generate_heart_odds == 0:
            love_bomb_1 = love_bomb(random.randint(50, 500))
            love_bombs.add(love_bomb_1)
            love_bomb_1.create()
            if period_mode:
                love_bomb_1.set_health(4)
                love_bomb_1.set_speed(15)
    
        generate_a_comment_odds = random.randint(0, 350)
        if period_mode:
            generate_a_comment_odds=1
            
        if generate_a_comment_odds == 0:
            compliment_display.start_display()
            
    compliment_display.show()
    love_bombs.update()
    pygame.display.flip()

    if no_of_lives == 0:
        kill_all_love_bombs(love_bombs)
        did_you_win = False
        cause_i_cant_fix_bug(3)
        generate_hearts_rn = False

    if kills_to_win <= 0:
        kill_all_love_bombs(love_bombs)
        did_you_win = True
        cause_i_cant_fix_bug(2)
        generate_hearts_rn = False

    clock.tick(20)
    pygame.display.set_caption('miss me? ;)')
    heart_test_rect = heart_open.get_rect()
    heart_test_rect.x = 100
    heart_test_rect.y = 100
    
    pygame.display.flip()

pygame.quit()
