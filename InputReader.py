class InputReader:

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
    
    def readInputFile(self):
        with open(self.fileLocation, "r") as inputFile:
            self.inputText = inputFile.read()
        return self.inputText
    
    def printInputText(self):
        print(self.inputText)