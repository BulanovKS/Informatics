import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


'''
x = [0,1,2,3,4]
y = [0,2.2,3.9,6.1,7.5]

x_app = [0,4]
y_app = [i*2 for i in x_app]
#y_app = [0,1,8]
plt.scatter(x,y)
plt.plot(x_app, y_app, 'y--')
plt.grid()
filename = input()
plt.savefig(f'./pics/{filename}.png', dpi=100)
plt.show()
'''
'''
x = [0,1,2,3,4]
y = [0,2.2,3.9,6.1,7.5]
y2 = y[::-1]
fig = plt.figure(figsize = (16,9)) # создали рисунок/Figure Fig пропорциями 16:9
ax1 = fig.add_subplot(221) # создали Axes (подграфик) ax1 в серии из 2 графиков, поставили на позицию [1,1] -- левый верхний угол
ax2 = fig.add_subplot(224)

ax1.plot(x,y, label = 'line1')
ax1.plot(x,y2, label = 'line2')
ax1.legend()
#ax2.plot(y,x, label = 'ax2')
xs = np.arange(0,4,0.001)

def func(x):
    return x*np.sin(x)


ax2.plot(xs,np.sin(1/xs))
ax1.set_title('graph 1')
ax2.set_title('graph 2')
ax1.set_xlabel('x1')
ax2.set_xlabel('x2')

plt.show()
'''


'''
dataframe = pd.read_csv('iris_data.csv')
print(dataframe.columns)
print(dataframe['Species'])
x_set1 = dataframe['SepalWidthCm'][:50]
y_set1 = dataframe['SepalLengthCm'][:50]

x_set2 = dataframe['SepalWidthCm'][50:100]
y_set2 = dataframe['SepalLengthCm'][50:100]

x_set3 = dataframe['SepalWidthCm'][100:]
y_set3 = dataframe['SepalLengthCm'][100:]
plt.plot(x_set1, y_set1,'*')
plt.plot(x_set2, y_set2,'*')
plt.plot(x_set3, y_set3,'*')
plt.xlim(0,100)
plt.title(r'$\frac{\alpha}{2}$')
plt.show()
'''