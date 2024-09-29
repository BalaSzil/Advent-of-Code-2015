from InputReader import InputReader

inputFile = InputReader("input2.txt")
uneditedInput = inputFile.getListWithLines()

from DayTwoPartOne import WrapperOrder

class RibbonOrder(WrapperOrder):
    
    def __init__(self, puzzleInput):
        super().__init__(puzzleInput)
        
    def getMaterialPerBox(self, line):
        length = int(line[0])
        width = int(line[1])
        height = int(line[2])
        ribbon = (2*length) + (2*width) + (2*height) - (2*max(length, width, height))
        bow = length * width * height
        lineTotal = ribbon + bow
        return lineTotal