from pylab import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\SIMLI.TTF", size=18)

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
def paintScatter(test,n2,data,n):
    # plt.figure()

#    plt.scatter(test[0],test[1],label="test")
    plt.scatter(data[0][0],data[0][1],label="A_label",marker='o',alpha='0.4')
    plt.scatter(data[1][0],data[1][1],label="B_label",marker='*',alpha='0.4')
    plt.scatter(data[2][0],data[2][1],label="C_label",marker='^',alpha='0.4')
    plt.scatter(data[3][0],data[3][1],label="D_label",marker='+',alpha='0.4')
    plt.legend()

    plt.title('SVM算法',fontproperties=font_set)
    plt.xlabel('x')
    plt.ylabel('y')
