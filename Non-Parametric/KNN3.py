'''
对三个测试点估计其分类结果
(-0.41, 0.82, 0.88),
(0.14, 0.72, 4.1),
(-0.81, 0.61, -0.38)
'''
import numpy as np
import pandas as pd
def read_data():
    data = pd.read_excel('data.xlsx')
    data = data.values
    return data


def get_distance(xi, X):
    dis = []
    for i in range(len(X)):
        dis.append(np.sqrt(np.sum(np.square(xi-X[i]))))
    return dis
'''
@:parameter test代表测试数据 一次一个
@:parameter X代表训练数据
'''
def knn(k, test, data):
    X = []
    for i in range(len(data)):
        X.append(data[i, :3])
    dis = get_distance(test, X)
    index = []
    index = np.argsort(dis)
    w = [0, 0, 0]
    for i in range(k):
        if data[index[i]][3] == 1:
            w[0] += 1
        if data[index[i]][3] == 2:
            w[1] += 1
        if data[index[i]][3] == 3:
            w[2] += 1
    if w[0] > w[1] and w[0] > w[2]:
        return "w1"
    if w[1] > w[0] and w[1] > w[2]:
        return "w2"
    if w[2] > w[0] and w[2] > w[1]:
        return "w3"


def main():
    data = read_data()
    k = 5
    test = [[-0.41, 0.82, 0.88], [0.14, 0.72, 4.1], [-0.81, 0.61, -0.38]]

    for i in range(len(test)):
        print(test[i])
        print("belong to", knn(k, test[i], data))

if __name__ == '__main__':
    main()