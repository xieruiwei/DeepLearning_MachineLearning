from pylab import *
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import confusion_matrix
"""
核心：SVM算法
n      - 共有几个训练数据集
n2     - 共有几个测试数据集
data   - 训练数据集
test   - 测试数据集
labels - 分类标签
author - 小k.o
modify_data
       - 2019-04-20
"""
def SVM(test,n2,data,n,labels,test_labels):
    train0 = np.c_[data[0][0][: n], data[0][1][: n]]
    test0 = np.c_[test[0][0][: n], test[0][1][: n]]

    train1 = np.c_[data[1][0][: n], data[1][1][: n]]
    test1 = np.c_[test[1][0][: n], test[1][1][: n]]

    train2 = np.c_[data[2][0][: n], data[2][1][: n]]
    test2 = np.c_[test[2][0][: n], test[2][1][: n]]

    train3 = np.c_[data[3][0][: n], data[3][1][: n]]
    test3 = np.c_[test[3][0][: n], test[3][1][: n]]

    train = np.r_[train0, train1, train2, train3]
    newtest = np.r_[test0, test1, test2, test3]
#    print(train)


    rbf_kernel_svm_clf = Pipeline((
        ("scaler", StandardScaler()),
        ("svm_clf", SVC(kernel="rbf", degree=3, coef0=1, C=5))
    ))
    rbf_kernel_svm_clf.fit(train, labels)

    predict = rbf_kernel_svm_clf.predict(newtest)

    # 准确率
    print(precision_score(test_labels, predict, average='micro'))
    # 混淆矩阵
    print(confusion_matrix(test_labels, predict))
