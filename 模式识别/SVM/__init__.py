from pylab import *
import SVM
import SVM_datas
import SVM_paintScatter
import sklearn
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import confusion_matrix

if __name__== '__main__':
    test, n2, data, n, labels,test_labels = SVM_datas.DataSet()
    SVM_paintScatter.paintScatter(test,n2,data,n)
    SVM.SVM(test,n2,data,n,labels,test_labels)
    plt.show()