from pylab import *
import perceptron
import perceptron_datas
import perceptron_paintScatter

if __name__== '__main__':
    test = [5,8]
    n,data1,data2,data3,labels = perceptron_datas.DataSet()
    perceptron_paintScatter.paintScatter(test,data1,data2,data3,n)
    perceptron.perceptron(test,data1,data2,data3,n,labels)
    plt.show()    #画图展示要在最后才能展示
