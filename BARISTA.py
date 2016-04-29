# my barista prototype. user uses arrow keys, the game tells them if they've done anything cool
# developements: put different shapes into seperate subroutines and make the computer work out what one
#               allow the user to chose the shapes they want to draw

import pygame
import sys
pygame.init()
pygame.key.set_repeat(5,1)
clock = pygame.time.Clock()

class coffeeImage():
    stage0 = pygame.image.load("stage0.jpg")
    stage1= pygame.image.load("stage1.png")
    stage2= pygame.image.load("stage2.png")
    done = pygame.image.load("stage3.png")
    def __init__(self):
        self.image = coffeeImage.stage0
        self.showing = "stage0"
        self.screen = pygame.Surface((97,90),0,32)
    def choseImage(self, stage):
        if self.showing == stage:
            return
        if stage == "stage0":
            self.image = coffeeImage.stage0
            self.showing = "stage0"
        if stage == "stage1":
            self.image = coffeeImage.stage1
            self.showing = "stage1"
        elif stage == "stage2":
            self.image = coffeeImage.stage2
            self.showing = "stage2"
        else:
            self.image = coffeeImage.done
            self.showing = "done"
    def draw(self):
        self.screen.fill(colours.white)
        self.screen.blit(self.image, (0,0) )


class colours():
    black = (0,0,0)
    white = (255,255,255)
    burgandy = (100,0,0)
    red = (255,0,0)
    green = (0,0,255)

class game():
    def __init__(self):
        self.windowWidth = 600
        self.windowHeight = 400
        self.window =pygame.display.set_mode((600,400))
        self.upCount = 0
        self.downCount = 0
        self.leftCount = 0
        self.rightCount = 0
        self.running = True
        self.drawingPicture= "stage0"

    def startup(self):
        self.headerFont = pygame.font.SysFont("comicsansms", 20)
        self.textFont = pygame.font.SysFont("comicsansms", 15)
        self.highlight = pygame.font.SysFont("comicsansms", 17)
        self.window.fill(colours.black)
        self.finishedAt = 0

    def DrawOnScreen(self, newText):
        header = "just start pouring!!"
        text = self.headerFont.render((header.title()), True, colours.burgandy)
        self.window.blit(text,(0,0))
        moreText= [["", (0,0)] for w in range(5)]
        moreText[0][0] = ("this is "+ newText).upper()
        moreText[0][1] = (0,50)
        moreText[1][0] = "use the arrow keys to practice latte art!"
        moreText[1][1] = (0,100)
        moreText[2][0] = "first hold down the up key"
        moreText[2][1] = (0,150)
        moreText[3][0] = "then hold down on the down key"
        moreText[3][1] = (0,200)
        moreText[4][0] = "to finish relise ur fingers!"
        moreText[4][1] = (0,250)
        subHeadings = []

        for x in range( len(moreText)):
            if self.drawingPicture == "stage0" and moreText[x][0] == "first hold down the up key":
                subHeadings.append( self.textFont.render(moreText[x][0],True, colours.black))
            elif self.drawingPicture == "stage1" and moreText[x][0] =="then hold down on the down key":
                subHeadings.append( self.textFont.render(moreText[x][0],True, colours.black))
            elif self.drawingPicture == "stage2" and moreText[x][0] =="to finish relise ur fingers!":
                subHeadings.append( self.textFont.render(moreText[x][0],True, colours.black))
            else:
                subHeadings.append( self.textFont.render(moreText[x][0],True, colours.burgandy))
            self.window.blit(subHeadings[x], moreText[x][1])
        myImages.draw()

    def getActions(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_UP:
                     self.upCount +=1
                     print("key up")
                 if event.key == pygame.K_DOWN:
                     self.downCount +=1
                     print("key down")
                 if event.key == pygame.K_LEFT:
                     self.leftCount +=1
                 if event.key == pygame.K_RIGHT:
                     self.rightCount +=1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.upCount = 0
                    print("stop")
                if event.key == pygame.K_DOWN:
                    self.downCount = 0
                if event.key == pygame.K_LEFT:
                    self.leftCount = 0
                if event.key == pygame.K_RIGHT:
                    self.rightCount = 0
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def makechanges(self):
        if self.upCount > 10:
            self.drawingPicture= "stage1"
        if self.downCount >15 and self.drawingPicture == "stage1":
            self.drawingPicture = "stage2"
        if self.downCount < 5 and self.drawingPicture == "stage2":
            self.drawingPicture = "done"
            pygame.time.wait(120)
            self.drawingPicture = "stage0"

        self.DrawOnScreen(self.drawingPicture)


    def refresh(self):
        self.window.blit(myImages.screen, (self.windowWidth - 97, self.windowHeight - 90))
        pygame.display.flip()
        self.window.fill(colours.white)

    def loop(self):
        self.startup()
        while self.running == True:
            self.getActions()
            myImages.choseImage(self.drawingPicture)
            self.makechanges() #update and draw
            self.refresh()

            clock.tick(5)

myImages = coffeeImage()
myGame = game()
myGame.loop()
