# Imports
import argparse

from software_1_0.fizzbuzz import fizzbuzz
from software_1_0.accuracy import accuracy
from software_2_0.model_train import model_train
from software_2_0.model_test import model_test
from software_2_0.model_accuracy import model_accuracy

# Extract command line argument
arg_parser = argparse.ArgumentParser(description= "Train model (default) or test data (provide file)")
arg_parser.add_argument("--test-data", dest="test_file", action="store", default=False)

argObj = arg_parser.parse_args()

# If argument is not present train the network, else test the network and record accuracy
if argObj.test_file == False:
    model_train()
else:
    fizzbuzz(argObj.test_file)
    accuracy()
    model_test(argObj.test_file)
    model_accuracy()

