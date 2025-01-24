import random as Random
#gridSize*gridSize grid which is world 
#0,0 where the Agent will start the game
#one 2 random number will be generated from 1 to gridSize which is the location of the wumpus then from there the surrounding will the the Stench
#shoot,move

class World:

    gridSize=int(input("Enter World Size :")) 

    def __init__(self):
        self.world = [["" for _ in range(self.gridSize)] for _ in range(self.gridSize)]
    
    def place(self,row:int,col:int,effect:str):
        if row-1  >= 0 :        
            self.world[row-1][col]+=effect
        if row+1 < self.gridSize:
            self.world[row+1][col]+=effect
        if col+1 < self.gridSize:
            self.world[row][col+1]+=effect
        if col-1 >= 0:
            self.world[row][col-1]+=effect
    
    def pitSpawn(self):
        noPit=self.gridSize
        for i in range(noPit):
            row=Random.randrange(1,self.gridSize)
            col=Random.randrange(1,self.gridSize)
            if self.world[row][col]!="👾" and self.world[row][col]!="Gold" and self.world[row][col]!="Pit":
                self.world[row][col]="Pit"
                self.place(row,col,"༄")
            i-=1
        
    def goldSpawn(self):
        row=Random.randrange(1,self.gridSize)
        col=Random.randrange(1,self.gridSize)
        if self.world[row][col]!="👾" and self.world[row][col]!="Pit":
            self.world[row][col]="°˖✧"
        self.pitSpawn()
    
    def wumpusSpawn(self):
        wumpusCount=1
        while(wumpusCount):
            row=Random.randrange(1,self.gridSize)
            col=Random.randrange(1,self.gridSize)
            if (row!=1 or col!=0 ) and (row!=0 or col!=1):
                self.world[row][col]="👾"
                wumpusCount-=1

        self.place(row,col,"♨")
        self.goldSpawn()

    def returnMap(self):
        self.wumpusSpawn()
        # var=self.world
        # # print(var)
        return self.world,self.gridSize
    
    def printGrid(self):
        for i in self.world:
            print(i)
   

if __name__=="__main__":
    obj=World()
    val=obj.returnMap()
    obj.printGrid()