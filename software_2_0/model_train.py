import tensorflow as tf
import random

from software_2_0.generate_train_data import generate_train_data

# net par
NUM_DIGITS = 10
TRAIN_BEGIN = 101
TRAIN_END = 1001
CATEGORIES = 4
TRAIN_DATA_SIZE = TRAIN_END - TRAIN_BEGIN
NUM_HIDDEN_1 = 100
# MODEL_PATH "./"

# oar
LEARNING_RATE = 0.05
TRAINING_EPOCHS = 10000
BATCH_SIZE = 128

train_X, train_Y = generate_train_data(TRAIN_BEGIN, TRAIN_END, CATEGORIES, NUM_DIGITS)

tf.compat.v1.disable_eager_execution()

X = tf.compat.v1.placeholder(tf.float32, [None, NUM_DIGITS])
Y = tf.compat.v1.placeholder(tf.float32, [None, CATEGORIES])
pred_Y = tf.compat.v1.placeholder(tf.float32, [None, CATEGORIES])

weights = {
    'h1': tf.Variable(tf.random.truncated_normal([NUM_DIGITS, NUM_HIDDEN_1])),
    'out': tf.Variable(tf.random.truncated_normal([NUM_HIDDEN_1, CATEGORIES]))
}

biases = {
    'b1': tf.Variable(tf.random.truncated_normal([NUM_HIDDEN_1])),
    'out': tf.Variable(tf.random.truncated_normal([CATEGORIES]))
}

init = tf.compat.v1.global_variables_initializer()
saver = tf.compat.v1.train.Saver()


def model(x, weights, biases):
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)

    out_layer = tf.matmul(layer_1, weights['out']) + biases['out']
    return out_layer

pred_Y = model(X, weights, biases)

cost_function = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred_Y, Y))
training_step = tf.compat.v1.train.GradientDescentOptimizer(LEARNING_RATE).minimize(cost_function)

tf_session = tf.compat.v1.Session()
tf_session.run(init)

for epoch in range(TRAINING_EPOCHS):

    for start in range(0, len(train_X), BATCH_SIZE):
        end = start + BATCH_SIZE
        tf_session.run(training_step, feed_dict={X: train_X[start:end], Y: train_Y[start:end]})

    correct_prediction = tf.equal(tf.argmax(pred_Y, 1), tf.argmax(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    accuracy = tf_session.run(accuracy, feed_dict={X: train_X, Y: train_Y})

    if(epoch%50 ==0):
        print("Epoch: ", epoch, " Train accuracy: ", accuracy, "\n")

save_path = saver.save(tf_session, "./model/")
print("Model saved in \n", save_path)
