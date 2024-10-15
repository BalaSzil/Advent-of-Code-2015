from Day1.DayOnePartOne import FloorCounter

class BasementFinder(FloorCounter):
    
    def __init__(self, instructions, up_char="(", down_char=")"):
        super().__init__(instructions)

    def is_basement_entry(self):
        return self.current_floor == -1
    
    def calculate_basement_entry(self, parsed_instructions):
        for i, move in enumerate(parsed_instructions):
            self.change_floors(move)
            if self.is_basement_entry():
                self.current_step = i + 1
                return self.current_step
    
    def get_basement_entry(self):
        return self.current_step