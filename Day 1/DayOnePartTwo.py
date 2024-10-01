import sys
sys.path.insert(0, "C:/Users/Callipolis/Desktop/Programming/AoC2/Advent-of-Code-2015")
from InputReader import InputReader

input_reader = InputReader("input1.txt")
raw_input = input_reader.get_raw_input()

from DayOnePartOne import FloorCounter

class BasementIndexFinder(FloorCounter):
    
    def __init__(self, puzzle_input):
        super().__init__(puzzle_input)

    def is_basement_entry(self):
        return self.current_floor == -1
    
    def count_floors(self):
        for i, move in enumerate(self.puzzle_input):
            self.change_floor(move)
            if self.is_basement_entry():
                self.current_step = i + 1
                break
    
    def get_basement_entry_step(self):
        return self.current_step



solution = BasementIndexFinder(raw_input)
print(solution.get_basement_entry_step())