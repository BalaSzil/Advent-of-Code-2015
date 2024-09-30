import sys
sys.path.insert(0, "C:/Users/Callipolis/Desktop/Programozás/AoC2/Advent-of-Code-2015")
from InputReader import InputReader

input_file = InputReader("input2.txt")
raw_input = input_file.get_list_with_lines()

from DayTwoPartOne import WrapperOrder

class RibbonOrder(WrapperOrder):
    
    def __init__(self, puzzle_input):
        super().__init__(puzzle_input)
        
    def get_material_per_box(self, line):
        length = int(line[0])
        width = int(line[1])
        height = int(line[2])
        ribbon = (2*length) + (2*width) + (2*height) - (2*max(length, width, height))
        bow = length * width * height
        line_total = ribbon + bow
        return line_total



solution = RibbonOrder(raw_input)
print(solution.get_req_material())