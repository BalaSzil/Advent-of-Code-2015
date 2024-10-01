import sys
sys.path.insert(0, "C:/Users/Callipolis/Desktop/Programming/AoC2/Advent-of-Code-2015")
from InputReader import InputReader

input_reader = InputReader("input1.txt")
raw_input = input_reader.get_raw_input()

class FloorCounter:
    
    current_floor = 0
    puzzle_input = None
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.count_floors()
    
    def __str__(self):
        return "The solution is: " + str(self.current_floor)
    
    def change_floor(self, move):
        if move == "(":
            self.current_floor += 1
        elif move == ")":
            self.current_floor -= 1
        else:
            print("Input character not recognized: ", move)
        
    def count_floors(self):
        for move in self.puzzle_input:
            self.change_floor(move)
        
    def get_floor_count(self):
        return self.current_floor



floor_counter = FloorCounter(raw_input)
print(floor_counter.get_floor_count())