from pylab import *
"""
n      - 共有几个数据集
data1  - 数据集1
data2  - 数据集2
labels - 分类标签
author - 小k.o
modify_data
       - 2019-04-20
"""
def DataSet():
    n = 10000
    X1 = np.random.normal(2,0.5,n)
    Y1 = np.random.normal(2,0.5,n)
    data1 = np.zeros((n,2))
    data2 = np.zeros((n,2))
    labels = np.zeros((2*n,1))
    for i in range(n):
        data1[i][0] = X1[i]
        data1[i][1] = Y1[i]
        labels[i] = 1

    min = -3
    max = -2
    X2 = np.random.rand(2 * n) * (max - min) + min
    Y2 = np.random.rand(2 * n) * (max - min) + min
    for i in range(n):
        data2[i][0] = X2[i]
        data2[i][1] = Y2[i]
        labels[i+n] = 2

    return n,data1,data2,labels

