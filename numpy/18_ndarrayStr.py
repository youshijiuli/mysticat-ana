import numpy as np

#numpy.char.add()函数依次对两个数组的元素进行字符串连接
print('连接两个字符串:')
print(np.char.add(['hello'], [' xyz']))
print('连接示例:')
print(np.char.add(['hello','hi'], [' abc',' xyz']))
print('-----------------------------------------------------')
'''
连接两个字符串:
['hello xyz']
连接示例:
['hello abc' 'hi xyz']
'''

#numpy.char.multiply()函数执行多重连接
print (np.char.multiply('NumPy ',3))
print('-----------------------------------------------------')
# NumPy NumPy NumPy

'''
numpy.char.center()函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充
np.char.center(str,width,fillchar)
width: 长度
fillchar: 填充字符
'''
print (np.char.center('NumPy',20,fillchar='*'))
print('-----------------------------------------------------')
# *******NumPy********

#numpy.char.capitalize()函数将字符串的第一个字母转换为大写
print(np.char.title("who's using numpy?"))
print('-----------------------------------------------------')
# Who'S Using Numpy?

#numpy.char.lower()函数对数组的每个元素转换为小写
# 操作数组
print(np.char.lower(['BAIDU', 'GOOGLE']))
# 操作字符串
print(np.char.lower('BAIDU'))
print('-----------------------------------------------------')
'''
['baidu' 'google']
baidu
'''

#numpy.char.upper()函数对数组的每个元素转换为大写
# 操作数组
print(np.char.upper(['baidu', 'google']))
# 操作字符串
print(np.char.upper('baidu'))
print('-----------------------------------------------------')
'''
['BAIDU' 'GOOGLE']
BAIDU
'''

#numpy.char.split()通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格。
#分隔符默认为空格
print(np.char.split('i like numpy?'))
#分隔符为 .
print(np.char.split('www.baidu.com',sep='.'))
print('-----------------------------------------------------')
'''
['i', 'like', 'numpy?']
['www', 'baidu', 'com']
'''

#numpy.char.splitlines()函数以换行符作为分隔符来分割字符串，并返回数组。
#\n，\r，\r\n 都可用作换行符
print(np.char.splitlines('i\nlike numpy?'))
print(np.char.splitlines('i\rlike numpy?'))
print('-----------------------------------------------------')
'''
['i', 'like numpy?']
['i', 'like numpy?']
'''

#numpy.char.strip()函数用于移除开头或结尾处的特定字符
# 移除字符串头尾的a字符
print(np.char.strip('ashok arunooba', 'a'))
# 移除数组元素头尾的a字符
print(np.char.strip(['arunooba', 'admin', 'java'], 'a'))
print('-----------------------------------------------------')
'''
shok arunoob
['runoob' 'dmin' 'jav']
'''

#numpy.char.join()函数通过指定分隔符来连接数组中的元素或字符串
# 操作字符串
print(np.char.join(':', 'runoob'))
# 指定多个分隔符操作数组元素
print(np.char.join([':','-'],['runoob','google']))
print('-----------------------------------------------------')
'''
r:u:n:o:o:b
['r:u:n:o:o:b' 'g-o-o-g-l-e']
'''

#numpy.char.replace()函数使用新字符串替换字符串中的所有子字符串
print (np.char.replace ('i like google','oo','ee'))
print('-----------------------------------------------------')
# i like geegle

#numpy.char.encode()函数对数组中的每个元素调用 str.encode 函数。默认编码是 utf-8
#numpy.char.decode()函数对编码的元素进行 str.decode()解码
a = np.char.encode('老王你好')
print(a)
print (np.char.decode(a))
'''
b'\xe8\x80\x81\xe7\x8e\x8b\xe4\xbd\xa0\xe5\xa5\xbd'
老王你好
'''

