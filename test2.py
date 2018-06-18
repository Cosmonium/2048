from graphics import *
import random

gapWidth=10
tileWidth=100
num=4

win=GraphWin("2048", tileWidth*num+gapWidth*(num+1),tileWidth*num+gapWidth*(num+1))
win.setBackground("white")
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
    hasMerged=0   
    def drawTile(self):
        r=Rectangle(Point(self.x-tileWidth//2,self.y-tileWidth//2),Point(self.x+tileWidth//2,self.y+tileWidth//2))    
        r.setFill(color_dict[self.val])
        r.setWidth(0)
        r.draw(win)
        r=Rectangle(Point(r.getP1().getX()+1,r.getP1().getY()+1),Point(r.getP2().getX()+1,r.getP2().getY()+1))
        rText=Text(Point(self.x,self.y),str(self.val))
        if self.val!=0:
            rText.draw(win)
            
    def drawTileAnimated(self):
        r=Rectangle(Point(self.x-tileWidth//8,self.y-tileWidth//8),Point(self.x+tileWidth//8,self.y+tileWidth//8))
        while (r.getP1().getX())>(self.x-tileWidth//2):
            r.setFill(color_dict[self.val])
            r.setWidth(0)
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
    if newVal<8:            #
        newVal=2            #
    else:                   # Some probability thing I tried to get '4' to appear less often as '2'
        newVal=4            #
    tiles[i][j].val=newVal
    tiles[i][j].drawTileAnimated()

    
    
def drawBoard():
    r=Rectangle(Point(0,0),Point(tileWidth*num+gapWidth*(num+1),tileWidth*num+gapWidth*(num+1)))
    r.setFill("White")
    r.draw(win)
    for i in range(num):
        for j in range(num):
            tiles[i][j].drawTile()

            
def checkMovementPossibility(direction=0):
    #checks if any tile can be moved or merged
    # direction 1,2,3,4 :: up, left, down, right (wasd)
    if direction==1:
        for j in range(num):
            for i in range(1,num):
                if (tiles[i][j].val!=0 and tiles[i-1][j].val==0) or (tiles[i][j].val==tiles[i-1][j].val and tiles[i][j].val!=0 and tiles[i-1][j].hasMerged==0):
                    return 1
        return 0
    elif direction==2:
        for i in range(num):
            for j in range(1,num):
                if (tiles[i][j].val!=0 and tiles[i][j-1].val==0) or (tiles[i][j].val==tiles[i][j-1].val and tiles[i][j].val!=0 and tiles[i][j-1].hasMerged==0):
                    return 1
        return 0
    elif direction==3:
        for j in range(num):
            for i in range(num-2,-1,-1):
                if (tiles[i][j].val!=0 and tiles[i+1][j].val==0) or (tiles[i][j].val==tiles[i+1][j].val and tiles[i][j].val!=0 and tiles[i+1][j].hasMerged==0):
                    return 1
        return 0
    elif direction==4:
        for i in range(num):
            for j in range(num-2,-1,-1):
                if (tiles[i][j].val!=0 and tiles[i][j+1].val==0) or (tiles[i][j].val==tiles[i][j+1].val and tiles[i][j].val!=0 and tiles[i][j+1].hasMerged==0):
                    return 1
        return 0
    
def checkIndexWithCoordinate():
    #makes sure that the co-ordinates of a tile are in accordance with ther indices. If not, movement animation till coordinates are right
    for i in range(num):
        for j in range(num):
            if tiles[i][j].y!=((i*tileWidth)+(tileWidth//2)+(gapWidth*(i+1))) or tiles[i][j].x!=((j*tileWidth)+(tileWidth//2)+(gapWidth*(j+1))):
                return 0
    return 1
            
    

        
def animateMovement():
    while checkIndexWithCoordinate()==0:
        for i in range(num):
            for j in range(num):
                xx=tiles[i][j].x
                yy=tiles[i][j].y
                r=Rectangle(Point(xx-tileWidth//2,yy-tileWidth//2),Point(xx+tileWidth//2,yy+tileWidth//2))    
                r.setFill(color_dict[0])
                r.setWidth(0)
                if xx+10<((j*tileWidth)+(tileWidth//2)+(gapWidth*(j+1))):
                    tiles[i][j].x+=10
                elif xx-10>((j*tileWidth)+(tileWidth//2)+(gapWidth*(j+1))):
                    tiles[i][j].x-=10
                elif yy+10<((i*tileWidth)+(tileWidth//2)+(gapWidth*(i+1))):
                    tiles[i][j].y+=10
                elif yy-10>((i*tileWidth)+(tileWidth//2)+(gapWidth*(i+1))):
                    tiles[i][j].y-=10
                elif yy==((i*tileWidth)+(tileWidth//2)+(gapWidth*(i+1))) and xx==((j*tileWidth)+(tileWidth//2)+(gapWidth*(j+1))):
                    continue
                else:
                    tiles[i][j].y=((i*tileWidth)+(tileWidth//2)+(gapWidth*(i+1)))
                    tiles[i][j].x=((j*tileWidth)+(tileWidth//2)+(gapWidth*(j+1)))
                if tiles[i][j].val!=0:
                    r.draw(win)
                    tiles[i][j].drawTile()
                    

        
def up():
    hasMoved=0
    while checkMovementPossibility(1)==1:
        hasMoved=1
        for j in range(num):
            for i in range(1,num):
                if tiles[i-1][j].val==0 and tiles[i][j].val!=0:
                    tiles[i][j],tiles[i-1][j]=tiles[i-1][j],tiles[i][j]
                elif tiles[i-1][j].val==tiles[i][j].val and tiles[i][j].val!=0 and tiles[i-1][j].hasMerged==0:
                    tiles[i-1][j],tiles[i][j]=tiles[i][j],tiles[i-1][j]
                    tiles[i][j].val=0
                    tiles[i-1][j].hasMerged=1
                    tiles[i-1][j].val*=2
        animateMovement()
    if hasMoved:
        drawBoard()
        createRandomTile()
    for i in range(num):
        for j in range(num):
            tiles[i][j].hasMerged=0
            print(tiles[i][j].val,end='    ')
        print()
    print()
    print()
    
        
        
def left():
    hasMoved=0
    while checkMovementPossibility(2)==1:
        hasMoved=1
        for i in range(num):
            for j in range(1,num):
                if tiles[i][j-1].val==0 and tiles[i][j].val!=0:
                    tiles[i][j],tiles[i][j-1]=tiles[i][j-1],tiles[i][j]
                elif tiles[i][j-1].val==tiles[i][j].val and tiles[i][j].val!=0 and tiles[i][j-1].hasMerged==0:
                    tiles[i][j-1],tiles[i][j]=tiles[i][j],tiles[i][j-1]
                    tiles[i][j].val=0
                    tiles[i][j-1].hasMerged=1
                    tiles[i][j-1].val*=2
        animateMovement()
    if hasMoved:
        drawBoard()
        createRandomTile() 
    for i in range(num):
        for j in range(num):
            tiles[i][j].hasMerged=0
            print(tiles[i][j].val,end='    ')
        print()
    print()
    print()
            
        
def down():
    hasMoved=0
    while checkMovementPossibility(3)==1:
        hasMoved=1
        for j in range(num):
            for i in range(num-2,-1,-1):
                if tiles[i+1][j].val==0 and tiles[i][j].val!=0:
                    tiles[i][j],tiles[i+1][j]=tiles[i+1][j],tiles[i][j]
                elif tiles[i+1][j].val==tiles[i][j].val and tiles[i][j].val!=0 and tiles[i+1][j].hasMerged==0:
                    tiles[i+1][j],tiles[i][j]=tiles[i][j],tiles[i+1][j]
                    tiles[i][j].val=0
                    tiles[i+1][j].hasMerged=1
                    tiles[i+1][j].val*=2
        animateMovement()
    if hasMoved:
        drawBoard()
        createRandomTile() 
    for i in range(num):
        for j in range(num):
            tiles[i][j].hasMerged=0
            print(tiles[i][j].val,end='    ')
        print()
    print()
    print()
    
    
def right():
    hasMoved=0
    while checkMovementPossibility(4)==1:
        hasMoved=1
        for i in range(num):
            for j in range(num-2,-1,-1):
                if tiles[i][j+1].val==0 and tiles[i][j].val!=0:
                    tiles[i][j],tiles[i][j+1]=tiles[i][j+1],tiles[i][j]
                elif tiles[i][j+1].val==tiles[i][j].val and tiles[i][j].val!=0 and tiles[i][j+1].hasMerged==0:
                    tiles[i][j+1],tiles[i][j]=tiles[i][j],tiles[i][j+1]
                    tiles[i][j].val=0
                    tiles[i][j+1].hasMerged=1
                    tiles[i][j+1].val*=2
        animateMovement()
    if hasMoved:
        drawBoard()
        createRandomTile() 
    for i in range(num):
        for j in range(num):
            tiles[i][j].hasMerged=0
            print(tiles[i][j].val,end='    ')
        print()
    print()
    print()
    

    
            
    
    
def startGame():
    initTileProp()
    drawBoard()
    createRandomTile()
    createRandomTile()
    drawBoard()
    keyPress=win.getKey()
    while True:
        keyPress=win.getKey()
        if keyPress=="w" or keyPress=="Up":
            up()
        elif keyPress=="a" or keyPress=="Left":
            left()
        elif keyPress=="s" or keyPress=="Down":
            down()
        elif keyPress=="d" or keyPress=="Right":
            right()
        else:
            break
    
          
    
startGame()
