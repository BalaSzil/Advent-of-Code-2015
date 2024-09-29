from InputReader import InputReader

uneditedInput = InputReader("input1.txt")
uneditedInput = uneditedInput.readInputFile()

class parenthesisNavigation:
    
    def __init__(self, puzzleInput):
        self.puzzleInput = puzzleInput

    def initFloorcounter(self):
        self.floorcounter = 0
    
    def __str__(self):
        return "The solution is: " + str(self.floorcounter)
    
    def adjustFloorcounter(self, move):
        self.move = move
        if self.move == "(":
            self.floorcounter += 1
        elif self.move == ")":
            self.floorcounter -= 1
        else:
            print("Input character not recognized", self.move)
        
    def processMovements(self):
        for move in self.puzzleInput:
            self.adjustFloorcounter(move)
    
    def getFloorcount(self):
        return self.floorcounter