from InputReader import InputReader
from Day1.DayOnePartOne import FloorCounter
from Day1.DayOnePartTwo import BasementFinder

input_reader = InputReader("input1.txt")
raw_input = input_reader.get_raw_input()

floor_counter = FloorCounter(raw_input)
parsed_input = floor_counter.parse_input()
floor_counter.count_floors(parsed_input)
print("The final floor at the end of the input:", floor_counter.get_final_floor())

basement_index_finder = BasementFinder(raw_input)
basement_index_finder.calculate_basement_entry(parsed_input)
print("The step at which Santa enters the basement:", basement_index_finder.get_basement_entry())

robs_challenged1 = FloorCounter("(((-2)+6((")
robs_challenged1_input = robs_challenged1.parse_input()
robs_challenged1.count_floors_with_skips(robs_challenged1_input)
print("If Santa is lazy and uses an elevator, and is crazy and hates the number 8, the final floor is:", robs_challenged1.get_final_floor())

robs_challenged2 = FloorCounter("(((((((((((((((((((((((((((((((((((((((((((((")
robs_challenged2_input = robs_challenged2.parse_input()
robs_challenged2.count_floors_with_skips(robs_challenged2_input, ["13", "20", "45", "81"])
print("If Santa hates them floors:", robs_challenged2.get_final_floor())