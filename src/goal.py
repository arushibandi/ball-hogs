import pygame
import random

#OVERVIEW:
#create a goal by first creating the goal group -- goals = pygame.sprite.Group()
#then add the type of goal you want and where it should be on the screen.
#For example, for a moving goal on the right side of the screen:
#right = MovingGoal(goalWidth,goalHeight,xPosition,yPosition, speed). x and y should be set to where the center of the goal should be
#goals.add(right) will put the right goal in your goals group
#goals.draw(screen) will draw the goals on the screen, after screen is created (screen.fill(colors))
class Goal(pygame.sprite.Sprite):
    
    #this function will draw the goals
    def __init__(self,  goalWidth, goalHeight, x, y):
        #first send the new goal object to the sprite superclass
        super(Goal, self).__init__()
        
        self.x, self.y = x, y
        self.goalWidth = goalWidth
        self.goalHeight = goalHeight

        self.rect = pygame.Rect(x - self.goalWidth, y - self.goalHeight,
                                2 * self.goalWidth, 2 * self.goalHeight)
        
        #a surface is needed to place the goal on
        self.image = pygame.Surface((2 * self.goalWidth, 2 * self.goalHeight))  # make it transparent
        self.image = self.image.convert_alpha()
        #random colors
        
        self.image.fill((255,255,255))
        
    def getRect(self):  # GET REKT
        self.rect = pygame.Rect(self.x - self.goalWidth, self.y - self.goalHeight,
                                2 * self.goalWidth, 2 * self.goalHeight)
                                
    def getLocation(self):
        return goalWidth, self.goalHeight, self.x, self.y, self.speed

    def update(self, screenWidth, screenHeight):
        self.getRect()
    
        
class MovingGoal(Goal):
    def __init__(self,  goalWidth, goalHeight, x, y, speed):
        #first send the new goal object to the sprite superclass
        super(Goal, self).__init__()
        
        self.x, self.y = x, y
        self.speed = speed
        
        self.goalWidth = goalWidth
        self.goalHeight = goalHeight

        self.rect = pygame.Rect(x - self.goalWidth, y - self.goalHeight,
                                2 * self.goalWidth, 2 * self.goalHeight)
        
        #a surface is needed to place the goal on
        self.image = pygame.Surface((2 * self.goalWidth, 2 * self.goalHeight))  # make it transparent
        self.image = self.image.convert_alpha()
        #random colors
        
        self.image.fill((255,255,255))
        
    def getLocation(self):
        return goalWidth, self.goalHeight, self.x, self.y, self.speed
        
    def getRect(self):  # GET REKT
        self.rect = pygame.Rect(self.x - self.goalWidth, self.y - self.goalHeight,
                                2 * self.goalWidth, 2 * self.goalHeight)

    def update(self, screenWidth, screenHeight):
        self.y +=self.speed
        if(self.y+self.goalHeight>=screenHeight):
            self.y-=self.speed
            self.speed=-self.speed
        elif(self.y-self.goalHeight<=40):
            self.y-=self.speed
            self.speed=-self.speed
        self.getRect()
