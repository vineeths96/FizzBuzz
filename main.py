import argparse

from software_1_0 import fizzbuzz, accuracy
from software_2_0 import model_train, model_test, model_accuracy

arg_parser = argparse.ArgumentParser(description= "Train model (default) or test data (provide file)")
arg_parser.add_argument("--test-data", dest="test_file", action="store", default=False)

argObj = arg_parser.parse_args()

if argObj.test_file == False:
    model_train.Main()
else:
    fizzbuzz(argObj.test_file)
    accuracy.accuracy()
    model_test(argObj.test_file)
    model_accuracy()

