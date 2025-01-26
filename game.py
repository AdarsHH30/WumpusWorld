# map will be displayed by hiding all the boxed except (0,0)
# options will be given to the user to move left, right, up, down
# if based on the user movement the state of the box will be displayed
# when the user enters start then the game will be started
# user enters his move
# from types import List
# from public import *
from world import *
import subprocess


class Game:
    UP, DOWN, RIGHT, LEFT = "UP(W)", "DOWN(S)", "RIGHT(D)", "LEFT(A)"
    FIRE, MOVE, QUIT = "FIRE(F)", "MOVE(M)", "QUIT & DISPLAY(Q)"

    def __init__(self):
        self.map = [["𝍈𝍈𝍈𝍈𝍈" for _ in range(worldSize)] for _ in range(worldSize)]
        self.map[0][0] = ""

    def instructions(self):
        DIRECTION = "DIRECTION:"
        CONTROLS = "CONTROLS:"
        directions = f"{DIRECTION:>30}:{self.DOWN:>10}{self.UP:>8}{self.RIGHT:>10}{self.LEFT:>10}"
        controls = f"{CONTROLS:>28}:{self.MOVE:>10}{self.FIRE:>10}{self.QUIT:>20}"
        print(directions, "\n\n", controls, "\n\n")
        print(
            f"Gold -> {GLITTER}\t Wumpus -> {WUMPUS} \nStench -> {STENCH} \t breeze -> {BREEZE} \nPit -> {PIT}"
        )

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
    def wantToPlayAgain(self):
        answer = input("Want To Play Again(Enter Yes to Continue No to exit) .... ?\n")
        if answer.lower() == "yes":
            subprocess.run("clear")
            self.restartGame()
        else:
            exit()

    def winORloose(self, currentVal):
        if PIT in currentVal:
            # self.endGameMessage("AGENT IS KILLED BY FALLING INTO A PIT...:(")
            subprocess.run("clear")
            # f = open("pitfall.txt", "r")
            # print(f.read())
            with open("public/pitfall.txt", "r") as f:
                print(f.read())
            self.wantToPlayAgain()

        elif WUMPUS in currentVal:
            # self.endGameMessage("AGENT IS KILLED BY WUMPUS...:(")
            subprocess.run("clear")
            f = open("public/deadbywumpus.txt", "r")
            print(f.read())
            self.wantToPlayAgain()

        elif GLITTER in currentVal:
            subprocess.run("clear")
            f = open("public/win.txt", "r")
            print(f.read())
            self.endGameMessage("AGENT WON BY ACQUIRING GOLD .. :O")
            self.wantToPlayAgain()

        else:
            return False

    def padding(self):
        x = f"{"":<50}"
        print(x, end="")

    def printMap(self, row, col):
        x = f"{"":<50}"
        print(x, "-------" * worldSize)
        for i in range(worldSize):
            print(x, "|", end="")
            for j in range(worldSize):
                padding = f"{self.map[i][j]:<5}"
                if i == row and j == col:
                    print(agent, end=" |")
                else:
                    val = self.map[i][j]
                    padded = val.center(5)
                    print([padded], end=" |")
            print("\n", x, "-------" * worldSize)

    def printMap(self, row, col):
        x = f"{"":<50}"
        print(x, "-------" * worldSize)
        for i in range(worldSize):
            print(x, "|", end="")
            for j in range(worldSize):
                if i == row and j == col:
                    val = agent.center(5)
                    print(val, end=" |")
                else:
                    val = self.map[i][j]
                    padded = val.center(5)
                    print(padded, end=" |")
            print("\n", x, "-------" * worldSize)

    def displayMoves(self, moves):
        print("\n")
        print(f"{"Possible Directions :":>40}", end="")
        padded = f"{moves[0]:>5}"
        print(padded, end="")
        for i in range(1, len(moves)):
            s = moves[i]
            print(f"{s:>5}", end="")
        print("\n")

    def displayControls(self):
        CONTROLS = "CONTROLS :"
        controls = f"{CONTROLS:>29}{self.MOVE:>10}{self.FIRE:>10}{self.QUIT:>20}"
        print(controls, "\n")

    def readyTOfire(self, row, col):
        moves = self.listPossibleMove(row, col)
        self.displayMoves(moves)
        dir = f"{"ENTER THE DIRECTION TO Fire : ":>49}"
        agent_move = input(dir)
        # print("Agent move is :", agent_move)
        if agent_move.upper() not in moves:
            self.printMap(row, col)
            print("INVALID MOVE")
            return row, col
        r, c = self.updateRowCOl(row, col, agent_move.upper())
        if cave[r][c] == "(@-@)":
            WUMPUS = "(XoX)"
            self.map[r][c] = WUMPUS

            print("you killed it ")

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
        dir = f"{"ENTER THE DIRECTION TO MOVE : ":>49}"
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
        padding = f"{"":<20}"
        print(padding, "|----------------------------------------------------|")
        print(padding, f"{"| CURRENT LOCATION EFFECTS":<10}:", end="")
        if currentVal == "":
            print(" Noting")
        else:
            print(currentVal)
        print(padding, "|----------------------------------------------------|\n")

    def quitAndDIsplay(self, row, col):
        x = f"{"":<50}"
        print(x, "-------" * worldSize)
        for i in range(worldSize):
            print(x, "|", end="")
            for j in range(worldSize):
                val = cave[i][j]
                padded = val.center(5)
                print(padded, end=" |")
            print("\n", x, "-------" * worldSize)

    def agentMove(self, row: int, col: int):
        while True:
            currentVal = cave[row][col]
            self.effectDisplay(currentVal)
            if self.winORloose(currentVal):
                exit
            self.displayControls()
            ctrl = f"{"ENTER  YOUR CONTROL :":>40}"
            agent_move = input(ctrl)
            if agent_move.upper() == "F":
                self.readyTOfire(row, col)
            elif agent_move.upper() == "M":
                row, col = self.readyToMove(row, col)
            elif agent_move.upper() == "Q":

                self.quitAndDIsplay(row, col)
                break
            else:
                print("INVALID MOVE TRY again")

            subprocess.run("clear")

            self.printMap(row, col)

    def displayGame(self):
        self.instructions()
        # obj.printGrid()
        self.printMap(0, 0)
        self.agentMove(0, 0)

    def restartGame(self):
        self.__init__()
        self.displayGame()


if __name__ == "__main__":
    obj = World()
    cave, worldSize = obj.returnMap()
    # obj.resizeMap()
    gameObj = Game()
    gameObj.displayGame()
