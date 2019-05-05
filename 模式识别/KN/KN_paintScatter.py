from pylab import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\SIMLI.TTF", size=18)

"""
data1  - 数据集1
data2  - 数据集2
author - 小k.o
modify_data
       - 2019-04-20
"""
def paintScatter(test,data1,data2,n):
    plt.figure()
    plt.scatter(test[0],test[1],marker='o',label="test")
    plt.legend()
    plt.scatter(data1[:,0],data1[:,1],marker='o',label="A_label")
    plt.legend()
    plt.scatter(data2[:,0],data2[:,1],marker='o',label="B_label")
    plt.legend()
    plt.title('K-N近邻估计算法',fontproperties=font_set)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()