#import pygame and other files
import pygame
from circleshape import *

#create a class called Asteroid that inherits from CircleShape
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):