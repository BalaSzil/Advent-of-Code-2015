class BoxParser:
    
    raw_dimensions = None
    parsed_dimensions = []
    
    def __init__(self, raw_dimensions):
        self.raw_dimensions = raw_dimensions
        self.parsed_dimensions = []
    
    def parse_single_box(self, box, delimiter="x"):
        split_dimensions = box.split(delimiter)
        int_dimensions = tuple(int(s) for s in split_dimensions)
        return int_dimensions
    
    def is_tenth_line(self, floor, rob_wants_skipping=False):
        if rob_wants_skipping:
            return floor == 10
        else:
            return False
    
    def parse_all_boxes(self):
        for i, box in enumerate(self.raw_dimensions, 1):
            if self.is_tenth_line(i):
                continue
            parsed_box = self.parse_single_box(box)
            self.parsed_dimensions.append(parsed_box)
    
    def get_parsed_dimensions(self):
        return self.parsed_dimensions