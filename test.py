from graphics import *
import random

gapWidth=10
tileWidth=100
num=4

win=GraphWin("2048", tileWidth*num+gapWidth*(num+1),tileWidth*num+gapWidth*(num+1))

color_dict = {
    0: "gray", 
    2: "#e7e2da", 
    4: "#e7decf", 
    8: "#efdcbd", 
    16: "#f6d49c", 
    32: "#f1b85b", 
    64: "#e79613", 
    128: "#d5c8d4", 
    256: "#e5a9e1", 
    512: "#e34fda", 
    1024: "#e34f73", 
    2048: "#fa0541", 
    4096: "#a20128"
}

class tile:
    x=0
    y=0
    val=0
    def drawTile(self):
        r=Rectangle(Point(self.x-tileWidth//2,self.y-tileWidth//2),Point(self.x+tileWidth//2,self.y+tileWidth//2))    
        r.setFill(color_dict[self.val])
        r.draw(win)
        r=Rectangle(Point(r.getP1().getX()+1,r.getP1().getY()+1),Point(r.getP2().getX()+1,r.getP2().getY()+1))
        rText=Text(Point(self.x,self.y),str(self.val))
        if self.val!=0:
            rText.draw(win)
            
    def drawTileAnimated(self):
        r=Rectangle(Point(self.x-tileWidth//8,self.y-tileWidth//8),Point(self.x+tileWidth//8,self.y+tileWidth//8))
        while (r.getP1().getX())>(self.x-tileWidth//2):
            print(r.getP1().getX())
            r.setFill(color_dict[self.val])
            r.draw(win)
            r=Rectangle(Point(r.getP1().getX()-0.3,r.getP1().getY()-0.3),Point(r.getP2().getX()+0.3,r.getP2().getY()+0.3))
        rText=Text(Point(self.x,self.y),str(self.val))
        if self.val!=0:
            rText.draw(win)
        
tiles = [[tile() for j in range(num)] for i in range(num)]



def initTileProp():
    #Initialise midpoints of tiles 
    for i in range(num):
        for j in range(num):
            tiles[i][j].y=(i*tileWidth)+(tileWidth//2)+(gapWidth*(i+1))
            tiles[i][j].x=(j*tileWidth)+(tileWidth//2)+(gapWidth*(j+1))
    
    
    
def createRandomTile():
    i=0
    j=0
    while True:
        i=random.randint(0,num-1)
        j=random.randint(0,num-1)
        if tiles[i][j].val==0:
            break
    newVal=random.randint(0,10)
    if newVal<7:
        newVal=2
    else:
        newVal=4
    tiles[i][j].val=newVal
    tiles[i][j].drawTileAnimated()

    
    
def drawBoard():
    for i in range(num):
        for j in range(num):
            tiles[i][j].drawTile()
    
    
    
def startGame():
    initTileProp()
    drawBoard()
    createRandomTile()
    createRandomTile()
    drawBoard()
    
                        
def test():
    startGame()            
    win.getMouse()
test()