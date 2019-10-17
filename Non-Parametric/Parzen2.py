# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:50:06 2019

@author: Administrator
"""
import xlrd
import numpy as np
import pandas as pd
# 读取数据


def read_data():
    x = []
    data = xlrd.open_workbook("lab3_data.xlsx")
    table = data.sheets()[0]
    rows = table.nrows
    for i in range(1, rows):
        row_value = table.row_values(i)
        x.append(row_value)
    return x


def get_phi(test_x, xi, h):
    test_x = np.mat(test_x)
    xi = np.mat(xi)
    # 正常默认向量是行向量，而输入的是列向量，但是最终结果都是一个数，所以这里的转置不一样
    phi = np.exp(-(test_x - xi) * (test_x - xi).T / (2 * h * h))
    return phi


def get_px(test_x, X, h):
    phi = 0
    n = len(X)
    for i in range(n):
        phi += get_phi(test_x, X[i], h)
    px = phi * 3 / (4 * np.pi * n * np.power(h, 3))
    return px


def parzen(h, test, data):
    px = [0, 0, 0]#px长度代表的是类别
    print("h =", h)
    for j in range(len(test)):#对每个测试数据进行分类
        print("x =", test[j])
        for i in range(len(px)):
            xi = [x[:3] for x in filter(lambda x: x[3] == i + 1, data)]#取出读取的前三列数据，并第四列类别标签
            px[i] = get_px(test[j], xi, h)
            print("px", i + 1, "=", px[i])
        #哪个最大属于哪一类
        if px[0] > px[1] and px[0] > px[2]:
            print("belong to w1")
        if px[1] > px[0] and px[1] > px[2]:
            print("belong to w2")
        if px[2] > px[0] and px[2] > px[1]:
            print("belong to w3")


def main():
    data = np.array([
                   [0.28, 1.31, -6.2, 1],
                   [0.07, 0.58, -0.78, 1],
                   [1.54, 2.01, -1.63, 1],
                   [-0.44, 1.18, -4.32, 1],
                   [-0.81, 0.21, 5.73, 1],
                   [1.52, 3.16, 2.77, 1],
                   [2.2, 2.42, -0.19, 1],
                   [0.91, 1.94, 6.21, 1],
                   [0.65, 1.93, 4.38, 1],
                   [-0.26, 0.82, -0.96, 1],

                   [0.011, 1.03, -0.21, 2],
                   [1.27, 1.28, 0.08, 2],
                   [0.13, 3.12, 0.16, 2],
                   [-0.21, 1.23, -0.11, 2],
                   [-2.18, 1.39, -0.19, 2],
                   [0.34, 1.96, -0.16, 2],
                   [-1.38, 0.94, 0.45, 2],
                   [-0.12, 0.82, 0.17, 2],
                   [-1.44, 2.31, 0.14, 2],
                   [0.26, 1.94, 0.08, 2],

                   [1.36, 2.17, 0.14, 3],
                   [1.41, 1.45, -0.38, 3],
                   [1.22, 0.99, 0.69, 3],
                   [2.46, 2.19, 1.31, 3],
                   [0.68, 0.79, 0.87, 3],
                   [2.51, 3.22, 1.35, 3],
                   [0.6, 2.44, 0.92, 3],
                   [0.64, 0.13, 0.97, 3],
                   [0.85, 0.58, 0.99, 3],
                   [0.66, 0.51, 0.88, 3],
    ])
    test = [[0.5, 1.0, 0.0], [0.31, 1.51, -0.50], [-0.3, 0.44, -0.1]]
    h1 = 1
    h2 = 0.1

    parzen(h1, test, data)
    parzen(h2, test, data)


if __name__ == '__main__':
    main()
