import sys
sys.path.insert(0, "C:/Users/Callipolis/Desktop/Programozás/AoC2/Advent-of-Code-2015")
from InputReader import InputReader

input_file = InputReader("input1.txt")
raw_input = input_file.get_raw_input()

class ParenthesisNavigator:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.floor_counter = 0
    
    def __str__(self):
        return "The solution is: " + str(self.floor_counter)
    
    def change_floor(self, move):
        if move == "(":
            self.floor_counter += 1
        elif move == ")":
            self.floor_counter -= 1
        else:
            print("Input character not recognized: ", move)
        
    def count_floors(self):
        for move in self.puzzle_input:
            self.change_floor(move)
    
    def get_floor_count(self):
        self.count_floors()
        return f"Total floor count: {self.floor_counter}"



solution = ParenthesisNavigator(raw_input)
print(solution.get_floor_count())