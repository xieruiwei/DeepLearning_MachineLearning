from pylab import *
import MyKNN
import KNN_datas
import KNN_paintScatter

if __name__== '__main__':
    test = [-1,-1]
    n,data1,data2,labels = KNN_datas.DataSet()
    KNN_paintScatter.paintScatter(test,data1,data2,n)
    MyKNN.KNN(test,data1,data2,n,labels,20)
    plt.show()