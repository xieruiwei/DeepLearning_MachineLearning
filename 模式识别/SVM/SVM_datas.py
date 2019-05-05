from pylab import *
"""
n      - 共有几个训练数据集
n2     - 共有几个测试数据集
data   - 训练数据集
test   - 测试数据集
labels - 分类标签
author - 小k.o
modify_data
       - 2019-04-20
"""
def DataSet():
    n = 500
    n2 = 300
    m = 2
    z = 4
    data = np.ones((z,m,n))   #z=4, 2行5列
    test = np.ones((z,m,n2))
    labels = np.zeros((4*n,1))
    test_labels = np.zeros((4*n2,1))
    data[0][0] = np.random.normal(0, 1, n)
    data[0][1] = np.random.normal(0, 1, n)
    test[0][0] = np.random.normal(0, 1, n2)
    test[0][1] = np.random.normal(0, 1, n2)

    data[1][0] = np.random.normal(1, 1, n)
    data[1][1] = np.random.normal(4, 1.5, n)
    test[1][0] = np.random.normal(1, 1, n2)
    test[1][1] = np.random.normal(4, 1.5, n2)

    data[2][0] = np.random.normal(8, 2, n)
    data[2][1] = np.random.normal(5, 1, n)
    test[2][0] = np.random.normal(8, 2, n2)
    test[2][1] = np.random.normal(5, 1, n2)

    data[3][0] = np.random.normal(3, 0.5, n)
    data[3][1] = np.random.normal(3, 0.5, n)
    test[3][0] = np.random.normal(3, 0.5, n2)
    test[3][1] = np.random.normal(3, 0.5, n2)

#    print(data)
    for i in range(n):
        labels[i]=1
        labels[i+1*n] = 2
        labels[i+1*n] = 3
        labels[i+1*n] = 4

    for i in range(n2):
        test_labels[i]=1
        test_labels[i+1*n2] = 2
        test_labels[i+1*n2] = 3
        test_labels[i+1*n2] = 4
    return test,n2,data,n,labels,test_labels