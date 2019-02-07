from tensorflow.examples.tutorials.mnist import input_data
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

global minst
mnist = input_data.read_data_sets("mnist_data",one_hot=True)

def printdata(numA):
    if(mnist.train.images[numA,0]!=0): tmp=1
    else: tmp=0
    print(tmp,end='')
    for i in range(1,784):
        if(mnist.train.images[numA,i]!=0): tmp=1
        else: tmp=0
        print(tmp,end='')
        if (i+1)%28==0:  print()
    print()
    for i in range(0,10):
        if mnist.train.labels[numA,i]==1: print(i)

def pltimage(BB):
    imagedata=mnist.train.images[BB]
    imagedata=imagedata.reshape(28,28)
    print("imagedata class is ",type(imagedata))
    plt.imshow(imagedata,cmap='gray')
    plt.axis('off')
    plt.show()


print(mnist.train.images.shape,mnist.train.images.shape)
print("please input:")
AA=int(input());
printdata(AA);
print("one data is print")
pltimage(AA)


