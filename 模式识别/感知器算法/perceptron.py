from pylab import *
import matplotlib.pyplot as plt
import perceptron_paintScatter
"""
核心：感知器算法
n      - 共有几个训练数据
data1  - 数据集1
data2  - 数据集2
data3  - 数据集3
labels - 分类标签
author - 小k.o
modify_data
       - 2019-04-20
"""
def every_perceptron(data1,data2,n,start,end):
    w = mat([1,1,1])
    count = 1
    while(count>0):         #训练数据集  直到获取一个适合的感知器
        count = 0
        for i in range(n):  #训练第一个数据集
            temp = mat(data1[i]).T
            if(w*temp<=0):
                w = w + temp.T   #不符合的训练数据集做惩罚
                count = count+1
        #第二类别需要乘以 -1
        d2 = data2*-1
        for i in range(n):
            temp = mat(d2[i]).T
            if(w*temp<=0):
                w = w + temp.T
                count = count+1
    # print(w)
    # print(count)
    a = double(w[:,0])
    b = double(w[:,1])
    c = double(w[:,2])
    perceptron_paintScatter.paintLine(a,b,c,start,end)

    
def perceptron(test,data1,data2,data3,n,labels):
    #对每一个训练数据样本 变为增广型
    #本来是需要这样子操作的，但是本人目前还不会扩充数组
    #因此在读取数据集时变顺便将数组变为增广型了
    start1 = -5
    end1 = 5
    start2 = 3
    end2 = 20
    start3 = -5
    end3 = 5
    every_perceptron(data1, data2, n,start1,end1)
    every_perceptron(data2, data3, n,start2,end2)
    every_perceptron(data3, data1, n,start3,end3)



