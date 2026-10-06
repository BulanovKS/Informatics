import numpy as np
import matplotlib.pyplot as plt

bubble_array = []
insertion_array = []
selection_array = []
N_array = []

with open("slow_sorts.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array.append(float(stroke[2]))
        insertion_array.append(float(stroke[3]))
        selection_array.append(float(stroke[4]))
        N_array.append(int(stroke[1]))

bubble_np_array = np.log(np.array(bubble_array))
insertion_np_array = np.log(np.array(insertion_array))
selection_np_array = np.log(np.array(selection_array))
N_np_array = np.log(np.array(N_array))

fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

markers = {0: "s", 1: "o", 2: "x"}
labels = {0: "random", 1: "ordered", 2: "reversed"}

for i in range(3):
    ax[0, 0].plot(N_np_array[0:10], bubble_np_array[10*i:10*(i + 1)], color='blue', marker=markers[i], label=labels[i])
    ax[0, 1].plot(N_np_array[0:10], insertion_np_array[10*i:10*(i + 1)], color='red', marker=markers[i], label=labels[i])
    ax[1, 0].plot(N_np_array[0:10], selection_np_array[10*i:10*(i + 1)], color='green', marker=markers[i], label=labels[i])

ax[0, 0].set_title('Bubble sort')
ax[0, 1].set_title('Insertion sort')
ax[1, 0].set_title('Selection sort')

ax[1, 1].plot(N_np_array[0:10], bubble_np_array[0:10], color='blue', marker="s", label="bubble (random)")
ax[1, 1].plot(N_np_array[0:10], insertion_np_array[0:10], color='red', marker="s", label="insertion (random)")
ax[1, 1].plot(N_np_array[0:10], selection_np_array[0:10], color='green', marker="s", label="selection (random)")

ax[1, 1].set_title('Сравнение сортировок')

fig.supxlabel('lnN')
fig.supylabel('lnT')
ax[0, 0].legend()
ax[0, 1].legend()
ax[1, 0].legend()
ax[1, 1].legend()

fig.suptitle('Медленные сортировки -O0', fontsize=16, fontweight='bold')
plt.tight_layout()
fig.savefig('slow_sorts.png')
plt.show()