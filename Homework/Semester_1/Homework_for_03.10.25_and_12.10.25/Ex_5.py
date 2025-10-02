import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#Обработка данных

data = pd.read_csv('BTC_data.csv')
time_list = list(data['time'])
close_list = list(data['close'])
time_x = np.array([(time_list[i])[8:10]+"-"+(time_list[i])[5:7]+"-"+(time_list[i])[0:4] for i in range(len(time_list))])
close_y = np.array(close_list)
print(time_x)
print(close_y)

#Построение графика

plt.figure(figsize = (16,9))

plt.plot(time_x, close_y)
plt.title("Bitcoin cost (data)")

plt.show()