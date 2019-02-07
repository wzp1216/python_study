import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

global mnist
mnist=input_data.read_data_sets("mnist_data/",one_hot=True)


if __name__=="__main__":
    print(mnist.train.images.shape,mnist.train.labels.shape)
    print(mnist.test.images.shape,mnist.test.labels.shape)
    print(mnist.validation.images.shape,mnist.validation.labels.shape)
    print("------------------num is ok-------------------")
    sess=tf.InteractiveSession()
    x=tf.placeholder(tf.float32,[None,784])
    W=tf.Variable(tf.zeros([784,10]))
    b=tf.Variable(tf.zeros([10]))
    y=tf.nn.softmax(tf.matmul(x,W)+b)
    y1=tf.placeholder(tf.float32,[None,10])
    cross_entropy=tf.reduce_mean(-tf.reduce_sum(y1*tf.log(y),reduction_indices=[1]))
    train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
    tf.global_variables_initializer().run()
    for i in range(1000):
        batch_xs,batch_ys=mnist.train.next_batch(100)
        train_step.run({x: batch_xs,y1:batch_ys})
    correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y1,1))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    print(accuracy.eval({x:mnist.test.images,y1:mnist.test.labels}))


