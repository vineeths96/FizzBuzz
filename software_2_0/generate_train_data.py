import numpy as np

def binary(num, NUM_DIGITS):
    x_binary = np.empty([0])
    for index in range(NUM_DIGITS):
        x_binary = np.append(x_binary, num >> index & 1)

    return x_binary


def category(num):
    y_categorical = np.zeros([4])
    if num % 15 == 0:
        y_categorical[3] = 1
    elif num % 5 == 0:
        y_categorical[2] = 1
    elif num % 3 == 0:
        y_categorical[1] = 1
    else:
        y_categorical[0] = 1

    return y_categorical


def generate_train_data(TRAIN_BEGIN, TRAIN_END, CATEGORIES, NUM_DIGITS):
    TRAIN_DATA_SIZE = TRAIN_END - TRAIN_BEGIN
    X = np.zeros([TRAIN_DATA_SIZE, NUM_DIGITS])
    Y = np.zeros([TRAIN_DATA_SIZE, CATEGORIES])

    for num in range(TRAIN_BEGIN, TRAIN_END):
        x_binary = binary(num, NUM_DIGITS)
        y_category = category(num)

        index = num - TRAIN_BEGIN
        X[index] = x_binary
        Y[index] = y_category

    return X, Y
