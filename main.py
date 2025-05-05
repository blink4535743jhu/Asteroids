# this allows us to use code from the open-source library throughout this file
import pygame

#allows me to call a method to exit my game
import sys

#import the variables from constants.py and player / asteroid classes
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    #initialize pygame and set screen dimensions for the game
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    #create 2 groups named updatable and drawable
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    #set both groups as containers for the Player class
    Player.containers = (updatable, drawable)

    #set all groups as containers for the Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

    #set the updatable group as the container for the AsteroidField Class
    AsteroidField.containers = (updatable)

    #create an object of the player class
    player = Player(x, y)

    #create an object of the AsteroidField Class
    asteroid = AsteroidField()

    

    #create an infinite "game" loop that creates the GUI and keeps it open
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #call the update method to allow for player turning using the updatable container
        updatable.update(dt)

        for asteroid in asteroids:
            asteroid.collision(player)
            print("Game over!")
            sys.exit()

        #color the GUI black
        screen.fill("black")

        #draw objects in the drawable container to the screen
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        #This will set the GUI to run at 60fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()