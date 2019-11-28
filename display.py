import pygame
import sys

class Display():
    def __init__(self):
        pygame.init()
        size = w,h = 800, 600
        self.padSize = 20, 100
        self.ballSize = 20,20
        self.screen = pygame.display.set_mode(size)

        self.padL = pygame.Rect((int(40 - self.padSize[0]/2), int((h - self.padSize[1])/2)), self.padSize)
        self.padR = pygame.Rect((int(w-40 - self.padSize[0]/2), int((h - self.padSize[1])/2)), self.padSize)

        ballPos = (int((w-self.ballSize[0])/2),int((h-self.ballSize[1])/2))
        self.ball = pygame.Rect(ballPos, self.ballSize)
        
    def moveBall(self, x, y):
        ''' moves the Ball by the given x and y value (can be negative)'''
        self.ball.move_ip(x,y)

    def setBallPos(self, x, y):
        ''' sets the position of the Ball to the given Position '''
        self.ball.centerx = x
        self.ball.centery = y

    def getBallPos(self):
        ''' returns the position of the ball as a tuple (x,y) '''
        return self.ball.centerx, self.ball.centery

    def movePadLeft(self, y):
        ''' moves the left Pad by the given y value '''
        self.padL.move_ip(0,y)

    def movePadRight(self, y):
        ''' moves the right Pad by the given y value '''
        self.padR.move_ip(0,y)

    def setPadLeftPos(self, y):
        ''' sets the Position of the left Pad to the given y value '''
        self.padL.centery = y

    def setPadRightPos(self, y):
        ''' sets the Position of the right Pad to the given y value '''
        self.padR.centery = y

    def getPadLeftPos(self):
        ''' returns the y Position of the left Pad '''
        return self.padL.centery

    def getPadRightPos(self):
        ''' returns the y Position of the right Pad '''
        return self.padR.centery

    def update(self):
        ''' this method updates the screen and should be called every programm cycle '''
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        self.screen.fill((0,0,0))
        pygame.draw.rect(self.screen, (255,255,255), self.padL)
        pygame.draw.rect(self.screen, (255,255,255), self.padR)
        pygame.draw.rect(self.screen, (255,255,255), self.ball)
        
        pygame.display.update()

    def isUpPressed(self):
        return pygame.key.get_pressed()[pygame.K_UP]

    def isDownPressed(self):
        return pygame.key.get_pressed()[pygame.K_DOWN]