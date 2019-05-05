from pylab import *

"""
核心：K-N近邻估计算法
n      - 共有几个数据集
k      - K-N近邻估计算法中距离最小的k个点
data1  - 数据集1
data2  - 数据集2
labels - 分类标签
author - 小k.o
modify_data
       - 2019-04-20
"""
def KNN(test,data1,data2,n,labels,k):
    # np.tile 数组扩充函数
    # 第一个参数为要扩充的数组
    # 第二个参数的 前一个参数为扩充列数  后一个参数为扩充行数
    # 测试：
    #     test = [1,1]
    #     t1 = ([1,2],[2,3],[3,4])
    #     mat = np.tile(test,(3,2))
    #     print(mat)

    data = np.zeros((2*n,2))
    for i in range(n):
        data[i] = data1[i]
    for i in range(n,2*n):
        data[i] = data2[i-n]

    Mat = np.tile(test,(2*n,1))-data  #得到测试数据  （x-x1）(y-y1)的数组
    Mat = Mat**2                      #得到测试数据到数据集每一个点的平方
    Distance = Mat.sum(axis=1)        #sum=0，普通相加，sum(axis=0)每一列相加，sum(axis=1)，每一行相加
    Dis = Distance ** 0.5             #得到测试数据到数据集每一个点的距离
    sortDis = Dis.argsort()           # 元素从小到大排序后的索引值
    list = []                   # 定义一个记录类别次数的字典
    for i in range(k):
        voteIlabel = labels[sortDis[i]]  # 取出前k个元素的类别
        list.append(voteIlabel)
    label_A = list.count(1)
    label_B = list.count(2)
    if label_A>label_B :
        print("属于类别A")
    else :
        print("属于类别B")