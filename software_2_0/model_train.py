import tensorflow as tf

from software_2_0.generate_train_data import generate_train_data
#net par
NUM_DIGITS = 10
TRAIN_BEGIN = 101
TRAIN_END = 1001
CATEGORIES = 4
TRAIN_DATA_SIZE = TRAIN_END - TRAIN_BEGIN
NUM_HIDDEN_1 = 256
#MODEL_PATH "./"

# oar
LEARNING_RATE = 0.001
TRAINING_EPOCHS = 100
BATCH_SIZE = 100
DISPLAY_STEP =1

train_X, train_Y = generate_train_data(TRAIN_BEGIN, TRAIN_END, CATEGORIES, NUM_DIGITS)
#train_X, train_Y = shuffle(train_X, train_Y, random state = 1)

X = tf.placeholder(tf.int8, [NUM_DIGITS, TRAIN_DATA_SIZE])
Y = tf.placeholder(tf.int8, [CATEGORIES, TRAIN_DATA_SIZE])
