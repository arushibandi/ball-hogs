# this creates the ball class and related functions
import pygame
import random 

class Ball(pygame.sprite.Sprite):
    
    def __init__(self, xCenter, yCenter):
        super(Ball, self).__init__()
        self.radius = 10
        self.xCenter = xCenter
        self.yCenter = yCenter
        self.xSpeed = 5
        self.ySpeed = 5
        self.boost = False
        self.rect = pygame.Rect(xCenter - self.radius, yCenter - self.radius,
                                2 * self.radius, 2 * self.radius)
        self.image = pygame.Surface((2 * self.radius, 2 * self.radius), 
        pygame.SRCALPHA) 
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, (255,255,112),
                           (self.radius, self.radius), self.radius)

    def getRect(self):  # GET REKT
        self.rect = pygame.Rect(self.xCenter - self.radius, self.yCenter - self.radius,2 * self.radius, 2 * self.radius)
                     
    def isWallCollision(self,screen):
        if (self.x<Center0 or self.x>screenWidth or self.yCenter<0 or 
        self.yCenter >screenHeight):
            update(self,screenWidth,screenHeight)
    
    def update(self, screenWidth, screenHeight):
        self.xCenter += self.xSpeed
        self.yCenter += self.ySpeed
        if self.xCenter < 0:
            self.xSpeed*=-1
        elif self.xCenter > screenWidth:
            self.xSpeed*=-1
        if self.yCenter < 0:
            self.ySpeed*=-1
        elif self.yCenter > screenHeight:
            self.ySpeed*=-1
        self.getRect()
    
    def getLocation(self):
        return [xCenter,yCenter]
