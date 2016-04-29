import pygame

class colours():
    black = (0,0,0)
    white = (255,255,255)
    burgandy = (100,0,0)
    red = (255,0,0)
    green = (0,0,255)
class shape():
    stage0 = pygame.image.load("stage0.jpg")
    maxStage = 10
    mistakes = 0
    misCount = 0
    def __init__(self):
        self.image =shape.stage0
        self.showing = "stage0"
        self.stage = 0
    def updateStage(self):
        self.stage +=1
    def newGame(self):
        del self
    def draw(self):
        self.screen.fill(colours.white)
        self.screen.blit(self.image, (0,0) )
    def checkStage(self):
        if self.stage >self.maxStage:
            return
        if self.stage == int(self.showing[5:]):
            return
    def sequence(self,u,d,r,l):
        if d ==l==r==u ==0 and self.stage>= self.maxStage:
            self.updateStage()
        if self.stage > self.maxStage + 30:
            print("your score for that was" + str(self.mistakes))
            self.__init__()
            self.newGame()

        self.misCount +=1
        if self.misCount >100:
            self.misCount  = 0
            print("new count")
        
class Heart(shape):
    stages= []
    stages.append("first hold down the up key")
    stages.append("then hold down on the down key")
    stages.append("to finish relise ur fingers!")
    stage1= pygame.image.load("stage1.png")
    stage2= pygame.image.load("stage2.png")
    stage3 = pygame.image.load("stage3.png")
    screen = pygame.Surface((97,90),0,32)
    maxStage =3
    def __init__(self):
        super().__init__()
    def checkStage(self):
        super().checkStage()
        if self.stage == 0:
            self.image = Heart.stage0
            self.showing = "stage0"
        elif self.stage ==1:
            self.image = Heart.stage1
            self.showing = "stage1"
        elif self.stage == 2:
            self.image = Heart.stage2
            self.showing = "stage2"
        else:
            self.image = Heart.stage3
            self.showing = "stage3"
    def sequence(self, upCount, downCount,r,l):
        super().sequence(upCount,downCount,r,l)
        if self.stage == 0 and upCount == 10:
            self.updateStage()
        elif downCount ==15 and self.stage == 1:
            self.updateStage()
        elif downCount == 0 and self.stage== 2:
            self.updateStage()
        if self.misCount == 0:
            if self.stage == 0 and [downCount !=0 or r != 0 or l !=0]:
                self.mistakes +=1
            elif self.stage ==1 and [upCount !=0 or r != 0 or l !=0]:
                self.mistakes +=1
            elif self.stage == 2 and [upCount !=0 or downCount !=0 or r != 0 or l !=0]:
                self.mistakes +=1
                
class Leaf(shape):
    stage1= pygame.image.load("leaf1.jpg")
    stage2= pygame.image.load("leaf2.jpg")
    stage3= pygame.image.load("leaf3.jpg")
    stage4 = pygame.image.load("leaf4.jpg")
    stage5 =pygame.image.load("leaf5.jpg")
    stage6 = pygame.image.load("leaf6.jpg")
    stage7 = pygame.image.load("leaf7.jpg")
    maxStage = 7
    stages = []
    stages.append("first press up to make a dot")
    stages.append("then go left")
    stages.append("then go right")
    stages.append("now go left again")
    stages.append("now go right again")
    stages.append("to end pull the jug down")
    stages.append("to finish realise your fingers!!")
    screen = pygame.Surface((97,90),0,32)
    def __init__(self):
        super().__init__()
    def checkStage(self):
        super().checkStage()
        if self.stage == 0:
            self.image = Leaf.stage0
            self.showing = "stage0"
        elif self.stage ==1:
            self.image = Leaf.stage1
            self.showing = "stage1"
        elif self.stage == 2:
            self.image = Leaf.stage2
            self.showing = "stage2"
        elif self.stage == 3:
            self.image = Leaf.stage3
            self.showing = "stage3"
        elif self.stage == 4:
            self.image = Leaf.stage4
            self.showing = "stage4"
        elif self.stage == 5:
            self.image = Leaf.stage5
            self.showing = "stage5"
        elif self.stage == 6:
            self.image = Leaf.stage6
            self.showing = "stage6"
        else:
            self.image = Leaf.stage7
            self.showing = "stage7"

    def sequence(self, u,d,r,l):
        super().sequence(u,d,r,l)

        if self.stage ==0: 
            if u == 10:
                self.updateStage()
            elif [d>0 or r>0 or l>0] and self.misCount == 0:
                self.mistakes +=1

        elif self.stage == 1 or self.stage == 3:
            if l == 10:
                self.updateStage()
            elif [u>0 or r>0 or l>0] and self.misCount == 0:
                self.mistakes +=1
                
        elif self.stage == 2 or self.stage == 4:
            if r == 10:
                self.updateStage()
            elif [u>0 or d>0 or l>0] and self.misCount == 0:
                self.mistakes +=1

        elif self.stage == 5:
            if d == 50:
                self.updateStage()
            elif [u>0 or d>0 or l>0] and self.misCount == 0:
                self.mistakes +=1
                
        elif self.stage>= 6:
            if d ==l==r==u ==0:
                self.updateStage()
            elif self.misCount == 0:
                self.mistakes +=1
                #_______________
        elif self.stage ==20:
            self.stage= 0
 
