import matplotlib.pyplot as plt
import pandas as pd

#Обработка данных

data = pd.read_csv('iris_data.csv')
species = list(data['Species'])
petal_l = list(data['PetalLengthCm'])

omega_1 = [0] * len(set(species))
k = 0
for i in list(set(species)):
    omega_1[k] = species.count(i) / len(species)
    k += 1

omega_2 = [0] * 3
for i in range(len(petal_l)-1):
    if petal_l[i] <= 1.2: omega_2[0] += petal_l[i]
    elif (petal_l[i] > 1.2) and (petal_l[i] <= 1.5): omega_2[1] += petal_l[i]
    elif petal_l[i] > 1.5: omega_2[2] += petal_l[i]

omega_3 = [omega_2[i] / len(petal_l) for i in range(0,3)]

#Построение диаграмм

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.pie(omega_1, labels = list(set(species)))
ax1.set_title('Species of irises')

ax2.pie([omega_3[0], omega_3[1], omega_3[2]], labels = ['less 1,2 cm','1,2 cm - 1,5 cm','more 1,5 cm'])
ax2.set_title('Length of petal (cm)')

plt.show()