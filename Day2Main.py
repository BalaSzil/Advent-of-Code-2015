from InputReader import InputReader
from Day2.WrappingPaperCalculator import WrappingPaperCalculator
from Day2.BoxParser import BoxParser
from Day2.BoxFactory import BoxFactory
from Day2.RibbonPaperCalculator import RibbonPaperCalculator

input_reader = InputReader("input2.txt")
raw_input = input_reader.get_list_with_lines()

box_parser = BoxParser(raw_input)
box_parser.parse_all_boxes()
parsed_box_dimensions = box_parser.get_parsed_dimensions()

box_factory = BoxFactory(parsed_box_dimensions)
box_factory.make_all_boxes()
ready_boxes = box_factory.get_finished_packaging()

wrapping_paper_calculator = WrappingPaperCalculator(ready_boxes)
wrapping_paper_calculator.calculate_total_paper()
print("Total wrapping material required:", wrapping_paper_calculator.get_required_paper())

ribbon_calculator = RibbonPaperCalculator(parsed_box_dimensions)
ribbon_calculator.calculate_total_box_ribbon()
print("Total ribbon material required:", ribbon_calculator.get_required_ribbon())



robs_challenged = BoxParser(["5x10", "10x5", "1x1"])
robs_challenged.parse_all_boxes()
parsed_robs_dimensions = robs_challenged.get_parsed_dimensions()
robs_factory = BoxFactory(parsed_robs_dimensions)
robs_factory.make_all_cylinders()
robs_suspicious_cylinders = robs_factory.get_finished_packaging()

robbing_paper_calculator = WrappingPaperCalculator(robs_suspicious_cylinders)
robbing_paper_calculator.calculate_total_cylinder_paper()
print("Total robbing paper required:", robbing_paper_calculator.get_required_paper())

ribi_robi_calculator = RibbonPaperCalculator(robs_suspicious_cylinders)
ribi_robi_calculator.calculate_total_cylinder_ribbon()
print("Total ribi-robi required:", ribi_robi_calculator.get_required_ribbon())