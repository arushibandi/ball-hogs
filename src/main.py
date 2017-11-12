
'''
pygamegame.py
created by Lukas Peraza
 for 15-112 F15 Pygame Optional Lecture, 11/11/15
- you might want to move the pygame.display.flip() to your 
 function,
    in case you don't need to update the entire display every frame (then you
    should use pygame.display.update(Rect) instead)
'''
import pygame
import socket
import scene
import goal
import ball

class BallHogz(object):

    def init(self):
        self.s = scene.Scene(self.width, self.height, "start", False)
        self.scores = [0,0]
        self.goals = pygame.sprite.Group()
        self.moving = False
        self.balls = pygame.sprite.Group()

    def mousePressed(self, x, y):
        if self.s.mode == "start" or self.s.mode == "end":
            self.s.mode = "game"

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if keyCode == 112:
            self.s.paused = not self.s.paused
        if(keyCode == pygame.K_m):
            self.moving = not self.moving

    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass

    def drawGoals(self, screen):
        #this draws the goals
        #TODO: ADD A BOOL TO SWITCH FROM MOVING AND STILL GOALS
        #the goal's width should fill 3/5ths of half the screen and height should be 1/5th of the screen
        goalWidth = self.height*.1
        goalHeight = self.width*.2
        xRight = goalWidth//2
        yRight = self.height//2
        
        xLeft = self.width - goalWidth//2
        yLeft = self.height//2
        if(self.moving):
            right = goal.MovingGoal(goalWidth, goalHeight, xRight,yRight, 2)
            left = goal.MovingGoal(goalWidth, goalHeight, xLeft,yLeft, 2)
        else:
            right = goal.Goal(goalWidth, goalHeight, xRight,yRight)
            left = goal.Goal(goalWidth, goalHeight, xLeft,yLeft)
            
        self.goals.add(right)
        self.goals.add(left)
     
    def drawBalls(self,screen):
        #this draws the ball
        xCenter = self.height//2
        yCenter = self.height//2
        
        self.balls = pygame.sprite.Group()
        ball1 = ball.Ball(xCenter,yCenter)
        self.balls.add(ball1)
        
    def redrawAll(self, screen):
        self.s.draw(screen)
        if(self.s.mode == "game"):
            self.goals.update(self.width, self.height)
            self.goals.draw(screen)
            self.balls.update(self.width,self.height)
            self.balls.draw(screen)

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=600, height=400, fps=50, title="Welcome to Ball Hogz!"):
        
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
    
        self.drawBalls(screen)
        self.drawGoals(screen)
        
        
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = BallHogz()
    game.run()

if __name__ == '__main__':
    main()
