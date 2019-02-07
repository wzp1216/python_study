import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

global mnist
mnist=input_data.read_data_sets("mnist_data/",one_hot=True)

def shownum(anum):
    anum=int(anum)
    num=mnist.train.images[anum]
    num=num.reshape(28,28)
    plt.imshow(num,cmap='gray')
    plt.axis('off')
    plt.show()

if __name__=="__main__":
    print(mnist.train.images.shape,mnist.train.labels.shape)
    print("------------------num is ok-------------------")
    print("please the number from 0--5500:")
    anum=input();
    while anum.isdigit():
        shownum(anum)
        print("input:",end="")
        anum=input()
    print("--------------quit----------------")


