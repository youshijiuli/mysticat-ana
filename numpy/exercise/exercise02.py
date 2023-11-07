import numpy as np

'''
生成1至25数字的5 X 5矩阵a1和1至20的5 X 4矩阵b，通过numpy的数组修改功能生成数组c,c数组打印结果如下:
[[ 1  2  3  4  5  1  2  3  4]
 [ 6  7  8  9 10  5  6  7  8]
 [11 12 13 14 15  9 10 11 12]
 [16 17 18 19 20 13 14 15 16]
 [21 22 23 24 25 17 18 19 20]]
'''
a=np.arange(1,26).reshape(5, 5)
b=np.arange(1,21).reshape(5, 4)
c=np.append(a,b, axis=1)
print(c)