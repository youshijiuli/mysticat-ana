from matplotlib import pyplot as plt
import numpy as np

'''
由3至19数字组成的数组作为x变量，通过公式y=3*x+11，画出如下点线图：
'''
x = np.arange(3,20)
y = 3*x+11
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,"ob")
plt.show()