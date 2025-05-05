#allow use of all variables from constants.py
from constants import *
#import the CircleShape parent class
from circleshape import CircleShape
#import the Shot method
from shot import Shot
#import pygame to be used by the Player class
import pygame

#Create a child class of CircleShape called Player
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    #override the draw method from the CircleShape class
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    #adjust player rotation speed
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    #This is a method provided by boot.dev... I updated it with more key commands and the time change for shot_timer
    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        

    #This method will allow the player sprite to move forward and backward
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    #This method will allow the player to shoot bullets
    def shoot(self):
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        
        shot = Shot(self.position.x, self.position.y)

        shot.velocity = pygame.Vector2(0, 1)
        shot.velocity = shot.velocity.rotate(self.rotation)
        shot.velocity = shot.velocity * PLAYER_SHOOT_SPEED