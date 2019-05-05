from pylab import *
import KN
import KN_datas
import KN_paintScatter

if __name__== '__main__':
    test = [-1,-1]
    n,data1,data2,labels = KN_datas.DataSet()
    KN_paintScatter.paintScatter(test,data1,data2,n)
    KN.KNN(test,data1,data2,n,labels,20)