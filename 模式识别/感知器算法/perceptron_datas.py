from pylab import *
"""
n      - 共有几个数据集
data1  - 数据集1
data2  - 数据集2
data3  - 数据集3
labels - 分类标签
author - 小k.o
modify_data
       - 2019-04-20
"""
def DataSet():
    n = 100
    X1 = np.random.normal(0,1,n)
    Y1 = np.random.normal(0,1,n)
    X2 = np.random.normal(15,1,n)
    Y2 = np.random.normal(0,1,n)
    X3 = np.random.normal(6,1,n)
    Y3 = np.random.normal(12,1,n)

    data1 = np.ones((n,3))
    data2 = np.ones((n,3))
    data3 = np.ones((n,3))
    labels = np.zeros((3*n,1))

    for i in range(n):
        data1[i][0] = X1[i]
        data1[i][1] = Y1[i]
        labels[i] = 1
        data2[i][0] = X2[i]
        data2[i][1] = Y2[i]
        labels[i+n] = 2
        data3[i][0] = X3[i]
        data3[i][1] = Y3[i]
        labels[i+n*2] = 3

    return n,data1,data2,data3,labels