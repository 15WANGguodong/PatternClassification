'''
只估计三个类别的概率密度函数
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def readData():
    data = pd.read_excel('data.xlsx')
    data = data.values
    return data


'''
@:parameter 二维数据跟一维相比求测试点与训练样本点之前的距离方式不变 
'''
def get_distiances(k, xi, X):
    dis = []
    for i in range(len(X)):
        dis.append(np.sqrt(np.sum(np.square(xi-X[i]))))
    dis.sort()
    return dis[k]


def knn(k, X):
    nums = 100
    '''二维数据,测试点也是二维'''
    x= y = np.linspace(-3, 4, nums)
    px = []
    mat_x = []
    for i in range(nums):
        for j in range(nums):
            mat_x.append([x[i], y[j]])
    for i in range(nums*nums):
        h = get_distiances(k, np.mat(mat_x)[i], X)
        px.append(k/(len(X)*np.pi*h*h))

    px2d = []
    for i in range(nums):
        list = []
        for j in range(nums):
            list.append(px[i * nums + j])
        px2d.append(list)
    px2d = np.array(px2d)

    x, y = np.meshgrid(x, y)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(x, y, px2d, rstride=1, cstride=1, cmap='rainbow')
    ax.set_xlabel("x1", color='r')
    ax.set_ylabel("x2", color='g')
    ax.set_zlabel("p(x)", color='b')
    plt.title("k=" + str(k))


def main():
    data = readData()
    xi = [x[:2] for x in filter(lambda x: x[3] == 3, data)]
    print(np.mat(xi).T)
    k1 = 1
    k2 = 3
    k3 = 5

    knn(k1, xi)
    knn(k2, xi)
    knn(k3, xi)

    plt.show()
if __name__ == '__main__':
    main()