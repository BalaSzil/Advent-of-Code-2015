class BoxFactory:
    
    packaging_dimensions = None
    finished_packaging = []
    
    def __init__(self, packaging_dimensions):
        self.packaging_dimensions = packaging_dimensions
        self.finished_packaging = []

    def make_box(self, length, width, height):
        side1 = length*width
        side2 = width*height
        side3 = height*length
        return (side1, side2, side3)
    
    def make_all_boxes(self):
        for box in self.packaging_dimensions:
            box_with_sides = self.make_box(*box)
            self.finished_packaging.append(box_with_sides)
    
    def make_cylinder(self, radius, height):
        return (radius, height)

    def make_all_cylinders(self):
        for cylinder in self.packaging_dimensions:
            cylinder_with_sides_tops_bottoms = self.make_cylinder(*cylinder)
            self.finished_packaging.append(cylinder_with_sides_tops_bottoms)
            
    def get_finished_packaging(self):
        return self.finished_packaging