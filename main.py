# this allows us to use code from the open-source library throughout this file
import pygame

#import the variables from constants.py
from constants import *

def main():
    #initialize pygame and set screen dimensions for the game
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #create an infinite "game" loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()

    #print information to the user regarding game initialization process
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()