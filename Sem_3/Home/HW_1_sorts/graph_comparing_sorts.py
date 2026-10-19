import numpy as np
import matplotlib.pyplot as plt

bubble_array_p = []
insertion_array_p = []

bubble_array_c = []
insertion_array_c = []

N_array_p = []
N_array_c = []

with open("python_sorts.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array_p.append(float(stroke[2]))
        insertion_array_p.append(float(stroke[3]))
        N_array_p.append(int(stroke[1]))

with open("slow_sorts.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array_c.append(float(stroke[2]))
        insertion_array_c.append(float(stroke[3]))
        N_array_c.append(int(stroke[1]))

bubble_np_array_p = np.log(np.array(bubble_array_p))
insertion_np_array_p = np.log(np.array(insertion_array_p))

bubble_np_array_c = np.log(np.array(bubble_array_c))
insertion_np_array_c = np.log(np.array(insertion_array_c))

N_np_array_p = np.log(np.array(N_array_p))
N_np_array_c = np.log(np.array(N_array_c))

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 8))

ax[0].plot(N_np_array_p, bubble_np_array_p, color='blue', marker="s", label="python")
ax[1].plot(N_np_array_p, insertion_np_array_p, color='red', marker="s", label="python")

ax[0].plot(N_np_array_c[0:10], bubble_np_array_c[0:10], color='blue', marker="o", label="c++")
ax[1].plot(N_np_array_c[0:10], insertion_np_array_c[0:10], color='red', marker="o", label="c++")

ax[0].set_title('Bubble sort')
ax[1].set_title('Insertion sort')

fig.supxlabel('lnN')
fig.supylabel('lnT')
ax[0].legend()
ax[1].legend()

fig.suptitle('Сравнение сортировок на C++ и Python -O0', fontsize=16, fontweight='bold')
plt.tight_layout()
fig.savefig('python_sorts.png')
plt.show()