import sys
sys.path.insert(0, "C:/Users/Callipolis/Desktop/Programozás/AoC2/Advent-of-Code-2015")
from InputReader import InputReader

input_file = InputReader("input1.txt")
raw_input = input_file.get_raw_input()

from DayOnePartOne import ParenthesisNavigator

class FindBasementEntry(ParenthesisNavigator):
    
    def __init__(self, puzzle_input):
        super().__init__(puzzle_input)

    def is_basement_entry(self):
        if self.floor_counter == -1:
            return True
        else:
            return False
    
    def count_floors(self):
        for i, move in enumerate(self.puzzle_input):
            self.change_floor(move)
            if self.is_basement_entry():
                self.current_floor = i + 1
                break
    
    def get_basement_entry_step(self):
        self.count_floors()
        return f"Basement is entered at step: {self.current_floor}"



solution = FindBasementEntry(raw_input)
print(solution.get_basement_entry_step())