import sys
from pygame.locals import *
import time
# initialize pygame
# Example file showing a basic pygame "game loop"
import pygame
from cardClass import *
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    deck1=deck()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("dark green")
    surface1=pygame.image.load(deck1.draw(1)[0].cardGraphic())
    screen.blit(surface1,(600,600))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
