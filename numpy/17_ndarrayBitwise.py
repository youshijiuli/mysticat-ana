import numpy as np

print('13 和 17 的二进制形式：')
a, b = 13,17
print(bin(a), bin(b))
print('13和17的位与:')
print(np.bitwise_and(13,17))
print('-----------------------------------------------------')
'''
13 和 17 的二进制形式：
0b1101 0b10001
13 和 17 的位与:
01101
10001 -->0001=1
'''

print('13和17的位或:')
print(np.bitwise_or(13,17))
'''
13和17的位或:
01101
10001 -->11101=29
'''
print('-----------------------------------------------------')

print('13的位反转，其中ndarray的dtype是uint8')
print(np.invert(np.array([13],dtype=np.uint8)))
# 比较 13和242的二进制表示
print('13 的二进制表示:')
print(np.binary_repr(13, width=8))
print('242 的二进制表示:')
print(np.binary_repr(242,width=8))
print('-----------------------------------------------------')
'''
13的位反转，其中ndarray的dtype是uint8
[242]
13 的二进制表示:
00001101
242 的二进制表示:
11110010
'''

#left_shift()函数将数组元素的二进制形式向左移动到指定位置，右侧附加相等数量的0
#right_shift()函数将数组元素的二进制形式向右移动到指定位置，左侧附加相等数量的0
print('10左移两位:')
print(np.left_shift(10,2))
print('40右移两位:')
print(np.right_shift(40,2))
print('10的二进制表示:')
print(np.binary_repr(10,width=8))
print('40的二进制表示:')
print(np.binary_repr(40,width=8))
'''
10左移两位:
40
10的二进制表示:
00001010
40的二进制表示:
00101000
'''
