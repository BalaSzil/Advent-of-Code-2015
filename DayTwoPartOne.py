from InputReader import InputReader

inputFile = InputReader("input2.txt")
uneditedInput = inputFile.getListWithLines()

class WrapperOrder:
    
    def __init__(self, puzzleInput):
        self.puzzleInput = puzzleInput

    def initPapercounter(self):
        self.papercounter = 0

    def lineToIterables(self, line):
        nums = line.split("x")
        return nums
    
    def getMaterialPerBox(self, line):
        length = int(line[0])
        width = int(line[1])
        height = int(line[2])
        side1 = length*width
        side2 = width*height
        side3 = height*length
        lineTotal = 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)
        return lineTotal
    
    def formatLines(self):
        self.initPapercounter()
        for line in self.puzzleInput:
            line = self.lineToIterables(line)
            lineTotal = self.getMaterialPerBox(line)
            self.papercounter += lineTotal 
    
    def getReqMaterial(self):
        self.formatLines()
        return self.papercounter