class InputReader:

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
    
    def readInputFile(self):
        with open(self.fileLocation, "r") as inputFile:
            self.inputText = inputFile.read()
    
    def getUneditedInput(self):
        self.readInputFile()
        return self.inputText
    
    def readInputWithLines(self):
        with open(self.fileLocation, "r") as inputFile:
            self.inputLines = [line.strip() for line in inputFile]
    
    def getListWithLines(self):
        self.readInputWithLines()
        return self.inputLines