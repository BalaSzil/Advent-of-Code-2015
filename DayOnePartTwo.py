from InputReader import InputReader

inputFile = InputReader("input1.txt")
uneditedInput = inputFile.getUneditedInput()

from DayOnePartOne import parenthesisNavigation

class FindBasementEntry(parenthesisNavigation):
    
    def __init__(self, puzzleInput):
        super().__init__(puzzleInput)

    def isBasementEntry(self):
        if self.floorcounter == -1:
            return True
        else:
            return False
    
    def processMovements(self):
        self.initFloorcounter()
        for i, move in enumerate(self.puzzleInput):
            self.adjustFloorcounter(move)
            if self.isBasementEntry():
                self.currentStep = i + 1
                break
    
    def getCurrentStep(self):
        self.processMovements()
        return self.currentStep