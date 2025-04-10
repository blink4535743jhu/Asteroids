# this allows us to use code from the open-source library throughout this file
import pygame

#import the variables from constants.py and player class from player.py
from constants import *
from player import *

def main():
    #initialize pygame and set screen dimensions for the game
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    #create an object of the player class
    player = Player(x, y)

    #create an infinite "game" loop that creates the GUI and keeps it open
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #call the update method to allow for player turning
        player.update(dt)

        #color the GUI black
        screen.fill("black")

        #draw the player on the screen
        player.draw(screen)

        pygame.display.flip()
        
        #This will set the GUI to run at 60fps
        dt = clock.tick(60) / 1000

    #print information to the user regarding game initialization process
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()