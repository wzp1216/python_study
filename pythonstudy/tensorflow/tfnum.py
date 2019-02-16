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
##创建一个对话；
    x=tf.placeholder(tf.float32,[None,784])
#创建数据空间，ＦＬＯＡＴ类型，不限数据条数，每个是２８＊２８即７８４；
    W=tf.Variable(tf.zeros([784,10]))
#Ｗ为７８４＊１０的变量，先全设置为０，每７８４个对一个数据；
    b=tf.Variable(tf.zeros([10]))
#先全置为０；
    y=tf.nn.softmax(tf.matmul(x,W)+b)
#使用ＳＯＦＴＭＡＸ算法，　Ｗ＊Ｘ＋Ｂ；　　　ＭＡＴＭＵＬ是ＴＦ中的乘法；
    y1=tf.placeholder(tf.float32,[None,10])
#开一个新的数据空间，y1是准确数据，y1  y 两者比较，用于计算偏差；哺乳
    cross_entropy=tf.reduce_mean(-tf.reduce_sum(y1*tf.log(y),reduction_indices=[1]))
#reduce_mean求结果均值；reduce_sum求和；y1*ln(y)  每次索引变化１
损失函数,交叉熵,Y1*LOG(Y),多个求和,小则准确;
#:cross_entropy=-tf.reduce_sum(y1*tf.log(y))也是一种简单损失函数写法;

    train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
#训练学习速率０。５　偏差函数cross_entropy
GRADIENTDESCENTOPTIMIZER梯度下降算法找最优,可以选择其他算法,
tf.global_variables_initializer().run()
#初始化变量并运行,每次SESSION启动前进行初始化工作;；
    for i in range(1000):
        batch_xs,batch_ys=mnist.train.next_batch(100)
#选择１００个样本训练，
        train_step.run({x: batch_xs,y1:batch_ys})
#训练字典 为X ,Y1 

correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y1,1)) 
#ARGMAX 返回张量里沿某轴的最高条目索引值;
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
#
    print(accuracy.eval({x:mnist.test.images,y1:mnist.test.labels}))

