import pygame

class Scene():
    def __init__(self, w , h, moving, mode="start", paused=False):
        self.w = w
        self.h = h
        self.mode = mode
        self.paused = paused
        self.board = pygame.Rect(0, 0, self.w, self.h)
        self.moving = moving
        
    def draw(self, screen, scores=[0,0]):
        if self.paused == True and self.mode == "game": self.drawPaused(screen)
        else:	
            if self.mode == "start": self.drawStart(screen)
            elif self.mode == "game": self.drawGame(screen, scores)
            elif self.mode == "end": self.drawEnd(screen)

    def drawStart(self, screen):
        pygame.font.init()
        f = pygame.font.SysFont('Comic Sans MS', 30)
        t1_size = f.size("Click anywhere to start playing!")
        t1 = f.render("Click anywhere to start playing!", False, (0, 230, 172))
        t2_size = f.size("Press 'p' to pause and 'e' to exit.")
        t2 = f.render("Press 'p' to pause and 'e' to exit.", False, (0, 230, 172))
       
        pygame.draw.rect(screen, pygame.Color(204, 255, 220), self.board)
        screen.blit(t1, (self.w/2 - t1_size[0]/2,self.h/2 - 2*t1_size[1]))
        screen.blit(t2, (self.w/2 - t2_size[0]/2,self.h/2 - t1_size[1]))
        if(self.moving):
            moving = "moving"
        else:
            moving = "still"
        moveS = "Toggle goals by pressing m. The current state is %s"%moving
        t3_size = f.size(moveS)
        t3 = f.render(moveS,False, (0, 230, 172))
        screen.blit(t3, (self.w/2 - t2_size[0]*.80,50))

        #pygame.draw.rect(screen, pygame.Color(0, 0, 0), (400,650,150,50))
        #pygame.draw.rect(screen, pygame.Color(0, 0, 0), (650,650,150,50))
        #pygame.draw.rect(screen, pygame.Color(0, 0, 0), (900,650,150,50))
        f1 = pygame.font.SysFont('Comic Sans MS Bold', 30)
        #t4_size = f.size("Choose a level of difficulty")
        #t4 = f.render("Choose a level of difficulty:", False, (0, 230, 172))
        #screen.blit(t4, (self.w/2 - t3_size[0]/2, self.h/2 + 2*t3_size[1]))
        #t5_size = f1.size("Beginner")
        #t5 = f1.render("Beginner", False, (255, 255, 255))
        #screen.blit(t5, (413,667))
        #t6_size = f1.size("Intermediate")
        #t6 = f1.render("Intermediate", False, (255, 255, 255))
        #screen.blit(t6, (663,667))
        #t7_size = f1.size("Advanced")
        #t7 = f1.render("Advanced", False, (255, 255, 255))
        #screen.blit(t7, (913,667))

    def drawGame(self, screen, scores):
        pygame.font.init()
        f = pygame.font.SysFont('Comic Sans MS', 30)
        s_left = f.render("Score: " + str(scores[0]), False, (0, 0, 0))
        left = pygame.Rect(0, 0, self.w/2, self.h)
        right = pygame.Rect(self.w/2, 0, self.w, self.h)
        pygame.draw.rect(screen, pygame.Color(173, 235, 235), left)
        pygame.draw.rect(screen, pygame.Color(255, 153, 153), right)
        screen.blit(s_left, (650,0))

    def drawEnd(self, screen):
        pygame.font.init()
        f = pygame.font.SysFont('Comic Sans MS', 30)
        t1_size = f.size("Thanks for playing! Click anywhere to start again!")
        t1 = f.render("Thanks for playing! Click anywhere to start again!", False, (0, 230, 172))
        pygame.draw.rect(screen, pygame.Color(204, 255, 220), self.board)
        screen.blit(t1, (self.w/2 - t1_size[0]/2,self.h/2))

    def drawPaused(self, screen):
        pygame.font.init()
        f = pygame.font.SysFont('Comic Sans MS', 30)
        t1_size = f.size("Press 'p' to unpause.")
        t1 = f.render("Press 'p' to unpause.", False, (0, 230, 172))
        pygame.draw.rect(screen, pygame.Color(204, 255, 220), self.board)
        screen.blit(t1, (self.w/2 - t1_size[0]/2,self.h/2))
