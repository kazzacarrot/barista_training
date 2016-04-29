# my barista prototype. user uses arrow keys, the game tells them if they've done anything cool
# developements: put different shapes into seperate subroutines and make the computer work out what one
#               allow the user to chose the shapes they want to draw, SCORE

import pygame
import sys, shapes

pygame.init()
pygame.key.set_repeat(5,1)
clock = pygame.time.Clock()

class chooseShape():
    n = 2
    Drawing = None
    moreText= [["", (0,0)] for w in range(4)]
    moreText[0][0] = ("okay so you can choose what you want to draw first")
    moreText[0][1] = (0,50)
    moreText[1][0] = "use the up and down arrow keys to chose"
    moreText[1][1] = (0,100)
    def drawOnScreen(window):
        header = "welcome to the 'be your own barrister game"
        text = myGame.headerFont.render((header.title()), True, colours.red)
        window.blit(text,(0,0))
        chooseShape.moreText[2][0] = "a Heart"
        chooseShape.moreText[2][1] = (0,200)
        chooseShape.moreText[3][0] = "a leaf"
        chooseShape.moreText[3][1] = (0,250)
        subHeadings = []
        for x in range( len(chooseShape.moreText)):
            if x == chooseShape.n:
                subHeadings.append(myGame.textFont.render(chooseShape.moreText[x][0],True, colours.black))
            else:
                subHeadings.append(myGame.textFont.render(chooseShape.moreText[x][0],True, colours.red))
            window.blit(subHeadings[x], chooseShape.moreText[x][1])

    def eventHandle(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                chooseShape.n -=1
            if event.key == pygame.K_DOWN:
                chooseShape.n +=1
            if event.key == pygame.K_RETURN:
                chooseShape.chosen(chooseShape.n)
            if chooseShape.n<2:
                chooseShape.n = 3
            elif chooseShape.n>3:
                chooseShape.n = 2
    def chosen(n):
        if n == 2 : #a heart has been chosen
            myGame.Drawing = shapes.Heart()
            myGame.chosen = True
        if n == 3: #a leaf has been chosen
            myGame.Drawing = shapes.Leaf()
            myGame.chosen = True

class colours():
    black = (0,0,0)
    white = (255,255,255)
    burgandy = (100,0,0)
    red = (255,0,0)
    green = (0,0,255)

class game():
    def __init__(self):
        self.windowWidth = 600          #the width of the main window
        self.windowHeight = 400         #the height of the main window
        self.window =pygame.display.set_mode((self.windowWidth,self.windowHeight)) #the main window

    def startup(self):
        self.headerFont = pygame.font.SysFont("comicsansms", 20)
        self.textFont = pygame.font.SysFont("comicsansms", 15)
        self.highlight = pygame.font.SysFont("comicsansms", 17)
        self.window.fill(colours.black)
        self.upCount = 0                ##the count of how many times we've gone up
        self.downCount = 0              #the count of how many times we've gone down
        self.leftCount = 0              #the count of how many times we've gone left
        self.rightCount = 0             #the count of how many times we've gone right
        self.running = True             #a bool to say if the game is running or not
        self.chosen = False         #a bool to say whether a shape has been chosen
        self.Drawing =None          #an object which is the picture
        self.killShape = False
        self.score = 0
    def DrawOnScreen(self):
        header = "just start pouring!!"
        text = self.headerFont.render((header.title()), True, colours.burgandy)
        self.window.blit(text,(0,0))
        moreText= [["", (0,0)] for w in range(2 + self.Drawing.maxStage)]
        moreText[0][0] = ("this is stage " + self.Drawing.showing)
        moreText[0][1] = (0,50)
        moreText[1][0] = "use the arrow keys to practice latte art!"
        moreText[1][1] = (0,100)
        for m in range(self.Drawing.maxStage):
            moreText[m+2][0] = self.Drawing.stages[m]
            moreText[m +2][1] = (0,150 + 50*m)
            if m >=5:               # m*50 +150 is greater than window height
                moreText[m +2][1] = (self.windowWidth/2,150 + (m-5)*50)
        subHeadings = []
        for x in range( len(moreText)):
            if moreText[x][0] == self.Drawing.stages[x-2] and self.Drawing.stage == x-2:
                subHeadings.append( self.textFont.render(moreText[x][0],True, colours.red))
            else:
                subHeadings.append( self.textFont.render(moreText[x][0],True, colours.burgandy))
            self.window.blit(subHeadings[x], moreText[x][1])
        self.Drawing.draw()
    def updateKeys(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.upCount +=1
            if event.key == pygame.K_DOWN:
                self.downCount +=1
            if event.key == pygame.K_LEFT:
                self.leftCount +=1
            if event.key == pygame.K_RIGHT:
                self.rightCount +=1
            if event.key == pygame.K_RETURN:
                self.chosen = False         #a bool to say whether a shape has been chosen
                self.Drawing =None          #an object which is the picture
                self.killShape = False
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                self.upCount = 0
            if event.key == pygame.K_DOWN:
                self.downCount = 0
            if event.key == pygame.K_LEFT:
                self.leftCount = 0
            if event.key == pygame.K_RIGHT:
                self.rightCount = 0
            if event.key == pygame.K_n:
                self.killShape = True
    def eventHandle(self,event):
        if self.chosen == False:
            chooseShape.eventHandle(event)
        else:
            self.updateKeys(event)
        if event.type == pygame.QUIT:
            self.running = False
            pygame.quit()
            sys.exit()

    def makechanges(self):
        self.Drawing.sequence(self.upCount, self.downCount, self.rightCount, self.leftCount)
        self.DrawOnScreen()
        if self.Drawing.stage == self.Drawing.maxStage:
            self.score -= self.Drawing.mistakes
            if self.Drawing.mistakes == 0:
                self.score  += 100
            elif self.Drawing.mistakes <self.Drawing.maxStage//2:
                self.score +=50
        print(self.score ,"you made", self.Drawing.mistakes, "mistakes")
        if self.killShape == True:
            self.Drawing.newGame()
            self.startup()

    def refresh(self):
        if self.chosen == True:
            self.window.blit(self.Drawing.screen, (self.windowWidth - 97, self.windowHeight - 90))
        pygame.display.flip()
        self.window.fill(colours.white)

    def loop(self):
        self.startup()
        while self.running == True:
            for event in pygame.event.get():
                self.eventHandle(event)     #event handling.
            if self.chosen == False:
                chooseShape.drawOnScreen(self.window)
            else:
                self.Drawing.checkStage()   #give me the right image
                self.makechanges()          # draw text and the image onto the screen
            self.refresh()                  #show the changes on the screen
            clock.tick(20)
myGame = game()
myGame.loop()
