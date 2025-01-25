import random as Random

# gridSize*gridSize grid which is world
# 0,0 where the Agent will start the game
# one 2 random number will be generated from 1 to gridSize which is the location of the wumpus then from there the surrounding will the the Stench
# shoot,move


WUMPUS = "👻"
PIT = "🕳️"
STENCH = "💨"
BREEZE = "༄"
GLITTER = "💰"
agent = "🤖"


class World:

    gridSize = 4

    def __init__(self):
        self.world = [["" for _ in range(self.gridSize)] for _ in range(self.gridSize)]

    def canPlace(self, check, effect, val):
        if effect not in val and val not in check:
            return True
        return False

    def place(self, row: int, col: int, effect: str):
        check = [WUMPUS, PIT]

        if row - 1 >= 0:
            if self.canPlace(check, effect, self.world[row - 1][col]):
                self.world[row - 1][col] += effect

        if row + 1 < self.gridSize:
            if self.canPlace(check, effect, self.world[row + 1][col]):
                self.world[row + 1][col] += effect

        if col + 1 < self.gridSize:
            if self.canPlace(check, effect, self.world[row][col + 1]):
                self.world[row][col + 1] += effect
        if col - 1 >= 0:
            if self.canPlace(check, effect, self.world[row][col - 1]):
                self.world[row][col - 1] += effect

    def pitSpawn(self):
        noPit = self.gridSize
        for i in range(noPit):
            row = Random.randrange(1, self.gridSize)
            col = Random.randrange(1, self.gridSize)
            if (
                WUMPUS not in self.world[row][col]
                and GLITTER not in self.world[row][col]
                and PIT not in self.world[row][col]
            ):
                self.world[row][col] = PIT
                self.place(row, col, BREEZE)
            i -= 1

    def goldSpawn(self):
        while True:
            row = Random.randrange(1, self.gridSize)
            col = Random.randrange(1, self.gridSize)
            if WUMPUS not in self.world[row][col]:
                print(row, col)
                self.world[row][col] = GLITTER
                break
        self.pitSpawn()

    def wumpusSpawn(self):
        row = Random.randrange(1, self.gridSize)
        col = Random.randrange(1, self.gridSize)
        self.world[row][col] = WUMPUS
        self.place(row, col, STENCH)
        self.goldSpawn()

    def returnMap(self):
        self.wumpusSpawn()
        # var=self.world
        # # print(var)
        return self.world, self.gridSize

    def resizeMap(self):
        for i in range(self.gridSize):
            for j in range(self.gridSize):
                if len(self.world[i][j]) == 2:
                    self.world[i][j] += " "
                elif len(self.world[i][j]) == 1:
                    self.world[i][j] = " " + self.world[i][j] + " "
                elif not len(self.world[i][j]):
                    self.world[i][j] = "  "

    def printGrid(self):
        self.resizeMap()
        for i in self.world:
            print(i)


if __name__ == "__main__":
    obj = World()
    obj.wumpusSpawn()
    obj.printGrid()
