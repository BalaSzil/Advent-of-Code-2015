class InputReader:

    def __init__(self, file_location):
        self.file_location = file_location
    
    def read_input_file(self):
        with open(self.file_location, "r") as input_file:
            self.input_text = input_file.read()
    
    def get_raw_input(self):
        self.read_input_file()
        return self.input_text
    
    def read_input_lines(self):
        with open(self.file_location, "r") as input_file:
            self.input_lines = [line.strip() for line in input_file]
    
    def get_list_with_lines(self):
        self.read_input_lines()
        return self.input_lines