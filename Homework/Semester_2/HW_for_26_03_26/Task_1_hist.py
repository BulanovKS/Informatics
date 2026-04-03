from matplotlib import pyplot as plt
import numpy as np

values = []

with open("english.txt", "r", encoding="utf_8") as file:
    for line in file:
        stroke = list(map(str, line.split()))
        values.append(int(stroke[-1]))

values_np = np.array(values)
plt.hist(values, color = 'red', edgecolor = 'red')
plt.xlabel("Длина пути")
plt.ylabel("Кол-во статей на данном удалении")
plt.title("Длина пути на статью 'Английский язык'")
plt.xticks(range(0, 6, 1))
plt.yticks(range(0, 16, 2))
plt.show()
