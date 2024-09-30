import sys
sys.path.insert(0, "C:/Users/Callipolis/Desktop/Programozás/AoC2/Advent-of-Code-2015")
from InputReader import InputReader

input_file = InputReader("input2.txt")
raw_input = input_file.get_list_with_lines()

class WrapperOrder:
    
    def __init__(self, puzzle_input):
        self.puzzle_input = puzzle_input
        self.paper_counter = 0

    def line_to_iterables(self, line):
        nums = line.split("x")
        return nums
    
    def get_material_per_box(self, line):
        length = int(line[0])
        width = int(line[1])
        height = int(line[2])
        side1 = length*width
        side2 = width*height
        side3 = height*length
        line_total = 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)
        return line_total
    
    def format_lines(self):
        for line in self.puzzle_input:
            line = self.line_to_iterables(line)
            line_total = self.get_material_per_box(line)
            self.paper_counter += line_total 
    
    def get_req_material(self):
        self.format_lines()
        return f"Total material required: {self.paper_counter}"



solution = WrapperOrder(raw_input)
print(solution.get_req_material())