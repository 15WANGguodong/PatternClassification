import xlrd
import numpy as np
import matplotlib.pyplot as plt


# 读取数据
def read_data():
    x = []
    data = xlrd.open_workbook("data.xlsx")
    table = data.sheets()[0]
    rows = table.nrows
    for i in range(1, rows):
        row_value = table.row_values(i)
        x.append(row_value)
    return x

'''
@:parameter k 代表样本点个数
@:parameter x 代表测试数据
@:parameter xi代表训练数据，也就是提高的样本点
计算每个测试点到所有样本点的距离，并对距离排序，取最小第K个距离点
'''
def get_distance(k, x, xi):
    dist = []
    for i in range(len(xi)):
        dist.append(np.sqrt(np.sum(np.square(x - xi[i]))))
    dist.sort()
    return dist[k]


def k_nn(k, xi):
    num = 1000
    x = np.linspace(0, 3, num)
    px = []
    for i in range(num):
        h = 2 * get_distance(k, x[i], xi)#乘以2是认为在特征是1维情况下，所在点的前后距离代表体积
        px.append(k / (len(xi) * h))#K/(N*V) V是代表小舱的体积，N是总的训练集样本点，K是选的K个点
    plt.subplot(1, 5, k)
    plt.plot(x, px)
    plt.xlabel("x")
    plt.ylabel("p(x)")
    plt.title("k=" + str(k))


def main():
    data = read_data()
    xi = [x[0] for x in filter(lambda x: x[3] == 3, data)]
    print(np.mat(xi).T)
    k1 = 1
    k2 = 3
    k3 = 5

    k_nn(k1, xi)
    k_nn(k2, xi)
    k_nn(k3, xi)

    plt.show()


if __name__ == '__main__':
    main()
