import os
import tensorflow as tf

from software_2_0.generate_train_data import generate_train_data

def model_train():
    # net par
    NUM_DIGITS = 10
    TRAIN_BEGIN = 101
    TRAIN_END = 1001
    CATEGORIES = 4
    NUM_HIDDEN_1 = 512
    NUM_HIDDEN_2 = 512

    # oar
    LEARNING_RATE = 0.01
    TRAINING_EPOCHS = 125
    BATCH_SIZE = 128
    DECAY = 1e-6
    MOMENTUM = 0.9

    train_X, train_Y = generate_train_data(TRAIN_BEGIN, TRAIN_END, CATEGORIES, NUM_DIGITS)

    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(NUM_HIDDEN_1, activation='relu', input_shape=[NUM_DIGITS]))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(NUM_HIDDEN_2, activation='relu'))
    model.add(tf.keras.layers.Dropout(0.2))
    model.add(tf.keras.layers.Dense(CATEGORIES, activation='softmax'))

    model.summary()

    #sgd = tf.keras.optimizers.SGD(lr=LEARNING_RATE, decay=DECAY, momentum=MOMENTUM, nesterov=True)

    model.compile(loss='categorical_crossentropy',
                  optimizer=tf.keras.optimizers.RMSprop(),
                  metrics=['accuracy'], #optimizer=sgd
                  )

    history = model.fit(train_X, train_Y,
                        batch_size=BATCH_SIZE,
                        epochs=TRAINING_EPOCHS,
                        verbose=1,
                        validation_data=(train_X, train_Y))

    try:
        os.makedirs("./model")
    except:
        pass

    model.save("./model/fizzbuzz.h5")

if __name__ == "__main__":
    model_train()