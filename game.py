
#map will be displayed by hiding all the boxed except (0,0)
#options will be given to the user to move left, right, up, down 
#if based on the user movement the state of the box will be displayed
#when the user enters start then the game will be started
# user enters his move 
from world import World 
# from types import List

class Game:
    
    def __init__(self,world,worldSize):
        self.map=[["####" for _ in range(worldSize)] for _ in range(worldSize)]
        self.map[0][0]=""
        self.WUMPUS="👾"
        self.PIT="🕳️"
        self.STENCH="♨"
        self.BREEZE="༄"
        self.GLITTER="°˖✧"
        

    def endGameMessage(message):
        print(message)
                 
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
            
    def listPossibleMove(self,row:int,col:int):
        arr=[]
        if col-1 >= 0:
            arr.append("W")
        if col+1 < worldSize:
            arr.append("S")
        if row-1  >= 0 :        
            arr.append("A")
        if row+1 < worldSize:
            arr.append("D")
        return arr
    

    def instructions(self):
        print("\nDIRECTIONS:")
        print("\n W - > UP \n S -> DOWN \n A -> LEFT \n D-> RIGHT\n")
        print("SIGNs:\n")
        print(f"Gold -> {self.GLITTER}\t Wumpus -> {self.WUMPUS} \nStench -> {self.STENCH} \t breeze -> {self.BREEZE} \nPit -> {self.PIT}")


    def updateRowCOl(self,row:int,col:int,move:str):
        if move == "A":
            return row-1,col
        elif move == "D":
            return row+1,col
        elif move == "S":
            return row,col+1
        elif move == "W":
            return row,col-1
        


        
    def agentMove(self,row,col):
        agentWon,agentLost=False,False

        while (not agentWon and not agentLost):
            currentLocation=cave[row][col]
            if currentLocation==self.PIT or (True if self.WUMPUS in currentLocation else False):
                agentLost=True
                self.endGameMessage("Agent Lost")
                break

            elif currentLocation==self.GLITTER:
                agentWon=True
                self.endGameMessage("Agent won by Acquiring the Gold")
                break
    
            else:
                moves=self.listPossibleMove(row,col)
                for move in moves:
                    print(move)
                agent_move=input("Enter your move::")
                if agent_move not in moves:
                    print("Invalid Move")
                    continue
                row,col=self.updateRowCOl(row,col,agent_move)
                print(row,col)

        

# class Agent:
#     def __init__(self):
        


if __name__=="__main__":
    obj=World()
    cave,worldSize=obj.returnMap()
    gameObj=Game(cave,worldSize)
    gameObj.instructions()
    obj.printGrid()
    gameObj.agentMove(0,0)
    