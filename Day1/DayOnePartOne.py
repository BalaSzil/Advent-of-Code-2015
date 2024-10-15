class FloorCounter:
    
    current_floor = 0
    instructions = None
    parsed_instructions = []
    going_up = None

    def __init__(self, instructions, up_char="(", down_char=")"):
        self.instructions = instructions
        self.up_char = up_char
        self.down_char = down_char
        self.parsed_instructions = []
        self.going_up = None

    def parse_character(self, character):
        if character == self.up_char:
            self.parsed_instructions.append(1)
        elif character == self.down_char:
            self.parsed_instructions.append(-1)
        elif character == "+":
            self.going_up = True
        elif character == "-":
            self.going_up = False
        elif character.isnumeric():
            character = int(character)
            if self.going_up:
                self.parsed_instructions.append(character)
            else:
                self.parsed_instructions.append(-abs(character))
        else:
            raise ValueError(f"Input character not recognized: {character}")

    def parse_input(self):
        for character in self.instructions:
            self.parse_character(character)
        return self.parsed_instructions

    def is_next_floor_skipped(self, skipped_floors, elevator_up=True):
        if elevator_up:
            return str(self.current_floor+1) in skipped_floors
        else:
            return str(self.current_floor-1) in skipped_floors
    
    def change_floors(self, move):
        self.current_floor += move

    def change_floors_with_skip(self, move, skipped_floors):
        if move > 0:
            for i in range(1, move+1):
                next_floor_must_be_skipped = self.is_next_floor_skipped(skipped_floors)
                if next_floor_must_be_skipped:
                    self.current_floor += 2
                else:
                    self.current_floor += 1
        else:
            for i in range(-1, move-1, -1):
                next_floor_must_be_skipped = self.is_next_floor_skipped(skipped_floors)
                if next_floor_must_be_skipped:
                    self.current_floor -= 2
                else:
                    self.current_floor -= 1

    def count_floors(self, parsed_instructions):
        for move in parsed_instructions:
            self.change_floors(move)
    
    def count_floors_with_skips(self, parsed_instructions, skipped_floors=["8"]):
        for move in parsed_instructions:
            self.change_floors_with_skip(move, skipped_floors)

    def get_final_floor(self):
        return self.current_floor