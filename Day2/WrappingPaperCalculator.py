from math import pi

class WrappingPaperCalculator:
    
    total_paper_required = 0
    packaging_dimensions = None
    
    def __init__(self, packaging_dimensions):
        self.packaging_dimensions = packaging_dimensions
    
    def calculate_paper_per_box(self, side1, side2, side3):
        wrapper_per_box = 2*side1 + 2*side2 + 2*side3 + min(side1, side2, side3)
        return wrapper_per_box
    
    def calculate_total_paper(self):
        for box in self.packaging_dimensions:
            self.total_paper_required += self.calculate_paper_per_box(*box)
    
    def calculate_paper_per_cylinder(self, radius, height):
        side = 2*radius*radius*pi + 2*radius*pi*height
        top_and_bottom = 2*radius*radius*pi
        return side + top_and_bottom
    
    def calculate_total_cylinder_paper(self):
        for cylinder in self.packaging_dimensions:
            self.total_paper_required += self.calculate_paper_per_cylinder(*cylinder)
    
    def get_required_paper(self):
        return self.total_paper_required