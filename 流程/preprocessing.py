#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   preprocessing.py
@Author  :   Cat 
@Version :   3.11
"""

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


"""feature_range 参数用于指定缩放后的特征值范围。
在这个例子中，MinMaxScaler 将特征值缩放到 3 到 5 之间。你需要传入一个元组，表示缩放后的最小值和最大值。例如："""


def minmax_demo():
    """数据归一化"""
    data = pd.read_csv(
        "./data/datingTestSet.csv",
        sep="\t",
        names=["milage", "Liters", "Consumtime", "label"],
    )
    print(data)
    print("============================")

    """[1000 rows x 4 columns]
    ============================"""
    # 1.实例化
    transfer = MinMaxScaler(feature_range=(3, 5))

    # 2.进行转换
    ret_data = transfer.fit_transform(data[["milage", "Liters", "Consumtime"]])
    print(f"归一化之后的数据：{ret_data}")

    """[[3.89665071 3.79610279 4.12466706]
    [3.31746519 3.68390933 4.97448832]
    [3.57085885 3.13785047 3.94899257]
    ...
    [3.58231898 4.01820587 4.02158985]
    [4.05422195 3.87330901 3.8580096 ]
    [3.95881586 3.75361819 4.57143608]]
        """


# 标准化
def stand_demo():
    """标准化"""
    data = pd.read_csv(
        "./data/datingTestSet.csv",
        sep="\t",
        names=["milage", "Liters", "Consumtime", "label"],
    )

    print(data)

    print("========================")

    # 1.实例化
    transfer = StandardScaler()

    # 2.进行转换
    ret_data = transfer.fit_transform(data[["milage", "Liters", "Consumtime"]])
    print("标准化之后的数据为:\n", ret_data)
    print("每一列的方差为:\n", transfer.var_)
    print("每一列的平均值为:\n", transfer.mean_)
    
    
#     标准化之后的数据为:
#  [[ 0.33193158  0.41660188  0.24523407]
#  [-0.87247784  0.13992897  1.69385734]
#  [-0.34554872 -1.20667094 -0.05422437]
#  ...
#  [-0.32171752  0.96431572  0.06952649]
#  [ 0.65959911  0.60699509 -0.20931587]
#  [ 0.46120328  0.31183342  1.00680598]]
# 每一列的方差为:
#  [4.81628039e+08 1.79902874e+01 2.46999554e-01]
# 每一列的平均值为:
#  [3.36354210e+04 6.55996083e+00 8.32072997e-01]


if __name__ == "__main__":
    # minmax_demo()
    print('hhh')
    stand_demo()
