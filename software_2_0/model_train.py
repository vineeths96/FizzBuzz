# Imports
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

from software_2_0.generate_train_data import generate_train_data
from software_2_0.model_parameters import *

def model_train():
    # Get the training data
    train_X, train_Y = generate_train_data(TRAIN_BEGIN, TRAIN_END, CATEGORIES, NUM_DIGITS)

    # Define the model
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(NUM_HIDDEN_1, activation='relu', input_shape=[NUM_DIGITS]))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(NUM_HIDDEN_2, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(CATEGORIES, activation='softmax'))

    model.summary()

    # Set model parameters
    model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.RMSprop(), metrics=['accuracy'])
    history = model.fit(train_X, train_Y, batch_size=BATCH_SIZE, epochs=TRAINING_EPOCHS, verbose=1, validation_data=(train_X, train_Y))

    # Try to create model directory
    try:
        os.makedirs("./model")
    except:
        pass

    # Save the model as h5 file
    model.save("./model/fizzbuzz.h5")


if __name__ == "__main__":
    model_train()