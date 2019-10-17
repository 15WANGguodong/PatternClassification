import numpy as np
import pandas as pd


def readData():
    data = pd.read_excel('data.xlsx', header=None)
    data = data.values
    return data

def get_phi(xi, test, h):
    xi = np.mat(xi)
    test = np.mat(test)
    phi = np.exp(-(test - xi) * (test - xi).T / (2 * h * h))
    return phi

def get_px(Xi, test, h):
    N = len(Xi)
    phi = 0
    for i in range(N):
        phi += get_phi(Xi[i], test, h)
    px = phi * 3 / (4 * np.pi * N * np.power(h, 3))
    return px
def parzen(train, test, h):
    #获取训练数据类别
    classes = np.zeros(shape=(3, ), dtype=float)#3代表数据的类别
    # classes = [0, 0, 0]
    for i in range(len(test)):
        for j in range(len(classes)):
            Xi = [x[:3] for x in filter(lambda x: x[3] == j + 1, train)]
            classes[j] = get_px(Xi, test[i], h)
            print("px", i + 1, "=", classes[j])
        print('belong to ', str(np.argmax(classes)+1))
        '''
        if classes[0] > classes[1] and classes[0] > classes[2]:
            print("belong to w1")
        if classes[1] > classes[0] and classes[1] > classes[2]:
            print("belong to w2")
        if classes[2] > classes[0] and classes[2] > classes[1]:
            print("belong to w3")
        '''


def main():
    data = readData()
    test = [[0.5, 1.0, 0.0], [0.31, 1.51, -0.50], [-0.3, 0.44, -0.1]]
    h1 = 1
    h2 = 0.1

    parzen(data, test, h1)
    parzen(data, test, h2)

if __name__ == '__main__':
    main()