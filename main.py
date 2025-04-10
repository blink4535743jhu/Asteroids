# this allows us to use code from the open-source library throughout this file
import pygame

#import the variables from constants.py
from constants import *

def main():
    #initialize pygame and set screen dimensions for the game
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    #create an infinite "game" loop that creates the GUI and keeps it open
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        
        #This will set the GUI to run at 60fps
        dt = clock.tick(60) / 1000

    #print information to the user regarding game initialization process
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()