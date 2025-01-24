
#map will be displayed by hiding all the boxed except (0,0)
#options will be given to the user to move left, right, up, down 
#if based on the user movement the state of the box will be displayed
#when the user enters start then the game will be started
# user enters his move 
from world import *
# from types import List

class Game:
    
    def __init__(self):
        self.map=[["####" for _ in range(worldSize)] for _ in range(worldSize)]
        self.map[0][0]=""
       
    def endGameMessage(self,message):
        print(message)
    
    
            
    def listPossibleMove(self,row:int,col:int):
        arr=[]
        
        if row+1 < worldSize:
            arr.append("S")
        if row-1 >=0:
            arr.append("W")
        if col+1 < worldSize:
            arr.append("D")
        if col-1 >= 0 :
            arr.append("A")

        return arr
    

    def instructions(self):
        print("\nDIRECTIONS:")
        print("\n W - > UP \n S -> DOWN \n A -> LEFT \n D-> RIGHT\n")
        print("SIGNs:\n")
        print(f"Gold -> {GLITTER}\t Wumpus -> {WUMPUS} \nStench -> {STENCH} \t breeze -> {BREEZE} \nPit -> {PIT}")


    def updateRowCOl(self,row:int,col:int,move:str):
        if move == "W":
            return row-1,col
        elif move == "S":
            return row+1,col
        elif move == "D":
            return row,col+1 
        elif move == "A":
            return row,col-1
        


    def winORloose(self,currentVal):
        if PIT in currentVal:
            self.endGameMessage("AGENT IS KILLED BY FALLING INTO A PIT...:(")

        elif WUMPUS in currentVal:
            self.endGameMessage("AGENT IS KILLED BY WUMPUS...:(")
                
        elif GLITTER in currentVal:
            self.endGameMessage("AGENT WON BY ACQUIRING GOLD .. :O")
        
        else:return False

    def printMap(self):
        print("|"+" "*(worldSize-1),end="")
        
        for i in range(worldSize):
            for j in range(worldSize): 
                print(self.map[i][j],end="  |  ")
            print("\n")
            # for x in range(worldSize):
            #     print("__"*worldSize,end="")
            print("\n")
            print("|   ",end="")
    

    def agentMove(self,row:int,col:int):

        while (True):
            currentVal=cave[row][col]
            if self.winORloose(currentVal):
                exit
 
            moves=self.listPossibleMove(row,col)
            
            for move in moves:
                print(move)
            agent_move=input("Enter your move::")
            if agent_move.upper() not in moves:
                print("Invalid Move")
                continue
            row,col=self.updateRowCOl(row,col,agent_move.upper())
            print(row,col)
            self.map[row][col]=cave[row][col]
            self.printMap()

if __name__=="__main__":
    obj=World()
    cave,worldSize=obj.returnMap()
    gameObj=Game()
    gameObj.instructions()
    gameObj.printMap()  
    gameObj.agentMove(0,0)
    