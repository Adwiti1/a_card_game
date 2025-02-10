import pygame
import os

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
space_pressed = False  # Flag to track space bar press

'''
#create a textbox on current frame
def textbox(sentence):
'''
    
    
    
# Define the function to update the background
image_no = 1
def update_background():
    global image_no
    default_image_size = (720, 720)
    bg_image = f"/Users/adwitibaranwal/Downloads/peterpan_images/{image_no}.png"
    
    # Assertion if file doesn't exist
    if not os.path.isfile(bg_image):
        raise AssertionError("This image doesn't exist")
        running = False
    
    imp = pygame.image.load(bg_image).convert()
    imp = pygame.transform.scale(imp, default_image_size)
    screen.blit(imp, (0, 0))
    pygame.display.flip()
    image_no += 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not space_pressed:
                update_background()
                space_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                space_pressed = False

    clock.tick(60)  # Limits FPS to 60
    pygame.display.set_caption('Tales of Neverland')

pygame.quit()
