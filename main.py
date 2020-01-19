import argparse

from software_1_0.fizzbuzz import fizzbuzz

arg_parser = argparse.ArgumentParser(description= "Train model (default) or test data (provide file)")
arg_parser.add_argument("--test-data", dest="test_file", action="store", default=False)

argObj = arg_parser.parse_args()
print(argObj.test_file)