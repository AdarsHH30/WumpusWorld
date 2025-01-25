# map will be displayed by hiding all the boxed except (0,0)
# options will be given to the user to move left, right, up, down
# if based on the user movement the state of the box will be displayed
# when the user enters start then the game will be started
# user enters his move
# from types import List
from world import *
import subprocess


class Game:
    UP, DOWN, RIGHT, LEFT = "UP(W)", "DOWN(S)", "RIGHT(D)", "LEFT(A)"
    FIRE, MOVE, QUIT = "FIRE(F)", "MOVE(M)", "QUIT(Q)"

    def __init__(self):
        self.map = [["𝍈𝍈𝍈" for _ in range(worldSize)] for _ in range(worldSize)]
        self.map[0][0] = ""

    def instructions(self):

        DIRECTION = "<< DIRECTION >>"
        CONTROLS = "<< CONTROLS >>"
        directions = f"{DIRECTION:>10}=>{self.DOWN:>20}{self.UP:>20}{self.RIGHT:>20}{self.LEFT:>20}"
        controls = f"{CONTROLS:>10}=>{self.MOVE:>30}{self.FIRE:>30}{self.QUIT:>30}"
        print(directions, "\n\n", controls)

    def endGameMessage(self, message):
        print(message)

    def listPossibleMove(self, row: int, col: int):
        arr = []

        if row + 1 < worldSize:
            arr.append("S")
        if row - 1 >= 0:
            arr.append("W")
        if col + 1 < worldSize:
            arr.append("D")
        if col - 1 >= 0:
            arr.append("A")
        return arr

    # def instructions(self):
    #     print("\nDIRECTIONS:")
    #     print("\n W - > UP \n S -> DOWN \n A -> LEFT \n D-> RIGHT\n")
    #     print("SIGNs:\n")
    #     print(
    #         f"Gold -> {GLITTER}\t Wumpus -> {WUMPUS} \nStench -> {STENCH} \t breeze -> {BREEZE} \nPit -> {PIT}"
    #     )

    def winORloose(self, currentVal):
        if PIT in currentVal:
            self.endGameMessage("AGENT IS KILLED BY FALLING INTO A PIT...:(")

        elif WUMPUS in currentVal:
            self.endGameMessage("AGENT IS KILLED BY WUMPUS...:(")

        elif GLITTER in currentVal:
            subprocess.run("clear")
            f = open("win.txt", "r")
            print(f.read())
            self.endGameMessage("AGENT WON BY ACQUIRING GOLD .. :O")
            exit()

        else:
            return False

    def padding(self):
        padding = f"{"":<50}"
        print(padding, end="")

    def printMap(self, row, col):
        print(self.padding(), "*", end="")
        for i in range(worldSize):
            print("-" * 3 + "*", end="")
        print("\n|", end="")
        for i in range(worldSize):
            self.padding()
            for j in range(worldSize):
                if i == row and j == col:
                    print(agent, end=" |")
                else:
                    print(self.map[i][j], end=" |")
            print("\n")

    def displayMoves(self, moves):
        print("\n   ")
        for s in moves:
            padded = f"{s:>50}"
            print(padded, end="")
        print("\n")

    def displayControls(self):
        CONTROLS = "<< CONTROLS >>"
        controls = f"{CONTROLS:>10}=>{self.MOVE:>30}{self.FIRE:>30}{self.QUIT:>30}"
        print(controls)

    def readyTOfire(self, row, col):
        moves = self.listPossibleMove(row, col)
        self.displayMoves(moves)
        dir = f"{"ENTER  THE DIRECTION TO FIRE >":>75}"
        if dir.upper() not in moves:
            self.printMap(row, col)
            print("INVALID MOVE")

    def updateRowCOl(self, row: int, col: int, move: str):
        match move:
            case "W":
                return row - 1, col
            case "S":
                return row + 1, col
            case "D":
                return row, col + 1
            case "A":
                return row, col - 1

    def readyToMove(self, row, col):
        moves = self.listPossibleMove(row, col)
        self.displayMoves(moves)
        dir = f"{"ENTER  THE DIRECTION TO MOVE >":>75}"
        agent_move = input(dir)
        print("Agent move is :", agent_move)
        if agent_move.upper() not in moves:
            self.printMap(row, col)
            print("INVALID MOVE")
            return row, col
        r, c = self.updateRowCOl(row, col, agent_move.upper())
        self.map[r][c] = cave[r][c]
        return r, c

    def effectDisplay(self, currentVal):
        padding = f"{"":<50}"
        print(padding, "---------------------------------------")
        print(padding, f"{"CURRENT LOCATION EFFECTS":<10}:", end="")
        if currentVal == "":
            print("Noting")
        else:
            print(currentVal)
        print(padding, "---------------------------------------")

    def agentMove(self, row: int, col: int):
        while True:
            currentVal = cave[row][col]
            self.effectDisplay(currentVal)
            if self.winORloose(currentVal):
                exit
            self.displayControls()
            ctrl = f"{"ENTER  YOUR CONTROL =":>75}"
            agent_move = input(ctrl)
            if agent_move.upper() == "F":
                self.readyTOfire(row, col)
            elif agent_move.upper() == "M":
                row, col = self.readyToMove(row, col)
            elif agent_move.upper() == "Q":
                obj.printGrid()
                break
            else:
                print("INVALID MOVE TRY again")
            subprocess.run("clear")
            self.printMap(row, col)

    def displayGame(self):
        self.instructions()
        self.printMap(0, 0)
        self.agentMove(0, 0)


if __name__ == "__main__":
    obj = World()
    cave, worldSize = obj.returnMap()
    obj.resizeMap()
    gameObj = Game()
    gameObj.displayGame()
