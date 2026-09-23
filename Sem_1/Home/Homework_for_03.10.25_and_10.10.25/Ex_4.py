import matplotlib.pyplot as plt
import pandas as pd

#Обработка данных

data = pd.read_csv('iris_data.csv')
sepal_l = list(data['SepalLengthCm'])
sepal_w = list(data['SepalWidthCm'])
petal_l = list(data['PetalLengthCm'])
petal_w = list(data['PetalWidthCm'])

#Построение графиков

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(231)
ax2 = fig.add_subplot(232)
ax3 = fig.add_subplot(233)
ax4 = fig.add_subplot(234)
ax5 = fig.add_subplot(235)
ax6 = fig.add_subplot(236)

ax1.scatter(sepal_l, sepal_w, color = 'red')
ax1.set_title('sepal length (sepal width)')

ax2.scatter(sepal_l, petal_l, color = 'orange')
ax2.set_title('sepal length (petal length)')

ax3.scatter(sepal_l, petal_w, color = 'yellow')
ax3.set_title('sepal length (petal width)')

ax4.scatter(sepal_w, petal_l, color = 'green')
ax4.set_title('sepal width (petal length)')

ax5.scatter(sepal_w, petal_w, color = 'blue')
ax5.set_title('sepal width (petal width)')

ax6.scatter(petal_l, petal_w, color = 'purple')
ax6.set_title('petal length (petal width)')

plt.show()