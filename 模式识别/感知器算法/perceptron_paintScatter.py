from pylab import *
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
font_set = FontProperties(fname=r"c:\windows\fonts\SIMLI.TTF", size=18)

"""
test   - 测试数据
data1  - 数据集1
data2  - 数据集2
data2  - 数据集3
author - 小k.o
modify_data
       - 2019-04-20
"""
def paintScatter(test,data1,data2,data3,n):
    # plt.figure()

    plt.scatter(test[0],test[1],label="test")
    plt.legend()
    plt.scatter(data1[:,0],data1[:,1],label="A_label")
    plt.legend()
    plt.scatter(data2[:,0],data2[:,1],label="B_label")
    plt.legend()
    plt.scatter(data3[:,0],data3[:,1],label="C_label")
    plt.legend()

    plt.title('感知器算法',fontproperties=font_set)
    plt.xlabel('x')
    plt.ylabel('y')


def paintLine(a,b,c,start,end):
    x = np.linspace(start,end)
    y = -(a/b)*x-(c/b)
    plt.plot(x,y)
    plt.legend()