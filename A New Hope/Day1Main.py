from Day1.BuildingNavigator import BuildingNavigator

with open("input1.txt", "r") as input_file:
    instructions = input_file.read()

building_navigator = BuildingNavigator(instructions)
building_navigator.traverse_building_to_end_of_input()
print(f"Santa arrives at floor {building_navigator.santas_current_floor}.")

building_navigator.reset_santa()
building_navigator.traverse_building_to_basement()
print(f"Santa enters the basement at step {building_navigator.floors_traversed}.")