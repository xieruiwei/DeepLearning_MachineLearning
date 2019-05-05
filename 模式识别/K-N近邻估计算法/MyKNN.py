from pylab import *


def KNN(test,data1,data2,n,labels,k):
    # 均匀分布概率密度图
    N = 10000
    range_1 = np.linspace(-4, 4, 1601)
    k1 = 1
    kn = 100

    p_m = []
    for i in range(len(range_1)):
        t = []
        for k in range(N):
            t.append(abs(range_1[i] - data2[k][0]))
        s = sorted(t)
        p_m.append(kn / N / s[kn] / 2)
    fig = plt.figure(figsize=(10, 10))
    # ax = fig.add_subplot(1,1,1)
    plt.plot(range_1, p_m)
    plt.xlim((-4, 1.5))
    plt.ylim((-0.15, 1.21))



    # 高斯分布概率密度图
    range_2 = np.linspace(-4, 4, 1601)
    p_g = []
    for i in range(len(range_2)):
        t = []
        for k in range(N):
            t.append(abs(range_2[i] - data1[k][0]))
        s = sorted(t)
        p_g.append(kn / N / s[kn] / 2)

    fig = plt.figure(figsize=(10, 10))
    # ax = fig.add_subplot(1,1,1)
    plt.plot(range_2, p_g)
    plt.xlim((0, 4))
    plt.ylim((-0.1, 1.2))