class BuildingNavigator:
    
    def __init__(self, instructions):
        self.instructions = instructions
        self.santas_current_floor = 0
        self.floors_traversed = 0
    
    def traverse_floor(self, instruction):
        if instruction == "(":
            self.santas_current_floor += 1
        elif instruction == ")":
            self.santas_current_floor -= 1
        else:
            raise ValueError("Your input contains an invalid character.\n"
                             "Input must contain only the following characters: '(', ')'.")
        
        self.floors_traversed += 1
            
    def traverse_building_to_end_of_input(self):
        for instruction in self.instructions:
            self.traverse_floor(instruction)
    
    def traverse_building_to_basement(self):
        for instruction in self.instructions:
            self.traverse_floor(instruction)
            if self.santas_current_floor == -1:
                break
    
    def reset_santa(self):
        self.santas_current_floor = 0
        self.floors_traversed = 0