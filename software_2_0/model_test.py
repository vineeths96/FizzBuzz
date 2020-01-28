# Imports
import os
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# Convert to binary sequence
def binary(num, NUM_DIGITS):
    x_binary = np.zeros([1, NUM_DIGITS])
    for index in range(NUM_DIGITS):
        x_binary[0, index] = (num >> index & 1)

    return x_binary

# Deencode the class and write it to file
def decategorize(cat, line):
    if cat == [0]:
        out_str = str(line)
    elif cat == [1]:
        out_str = "fizz\n"
    elif cat == [2]:
        out_str = "buzz\n"
    else:
        out_str = "fizzbuzz\n"

    return out_str


def model_test(fname):
    NUM_DIGITS = 10

    # Try opening the test file
    try:
        input_file = open(fname, 'r')
    except:
        print("Input file does not exist. Please try again.\n")
        exit()

    output_file = open("Software2.txt", 'w')

    # Try opening the model
    try:
        model = tf.keras.models.load_model("./model/fizzbuzz.h5")
    except:
        print("Trained model does not exist. Please train the model.\n")
        exit()

    # Find the output class and write it to file
    for line in input_file:
        line_binary = binary(int(line), NUM_DIGITS)
        pred_Y = model.predict_classes(line_binary)

        out_str = decategorize(pred_Y, line)
        output_file.write(out_str)

    # Close the files
    input_file.close()
    output_file.close()