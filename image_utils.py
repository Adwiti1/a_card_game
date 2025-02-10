import pygame
screen = pygame.display.set_mode((720, 720))

def my_update_image():
    default_image_size = (720, 720)
    imp = pygame.image.load("/Users/adwitibaranwal/Downloads/peterpan_images/opening_winner_mispelled.png").convert()
    imp = pygame.transform.scale(imp, default_image_size)
    screen.blit(imp, (0, 0))
    pygame.display.flip()