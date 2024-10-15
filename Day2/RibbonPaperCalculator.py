from math import pi

class RibbonPaperCalculator():
    
    total_ribbon_required = 0
    packaging_dimensions = None
    
    def __init__(self, packaging_dimensions):
        self.packaging_dimensions = packaging_dimensions
        self.total_ribbon_required = 0
        
    def calculate_ribbon_per_box(self, length, width, height):
        ribbon = (2*length) + (2*width) + (2*height ) - (2*max(length, width, height))
        bow = length * width * height 
        ribbon_for_box = ribbon + bow
        return ribbon_for_box
    
    def calculate_total_box_ribbon(self):
        for box in self.packaging_dimensions:
            self.total_ribbon_required += self.calculate_ribbon_per_box(*box)
    
    def calculate_ribbon_per_cylinder(self, radius, height):
        ribbon = (4*height) + (2*2*radius)
        bow = radius*radius*pi*height
        ribbon_for_cylinder = ribbon + bow
        return ribbon_for_cylinder
    
    def calculate_total_cylinder_ribbon(self):
        for cylinder in self.packaging_dimensions:
            self.total_ribbon_required += self.calculate_ribbon_per_cylinder(*cylinder)
    
    def calculate_wrapping_paper_from_ribbon(self, ribbon_percentage=0.2):
        return self.total_ribbon_required*ribbon_percentage
            
    def get_required_ribbon(self):
        return self.total_ribbon_required