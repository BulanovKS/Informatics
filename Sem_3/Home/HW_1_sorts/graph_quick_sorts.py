import numpy as np
import matplotlib.pyplot as plt

merge_array = []
quick_array = []
heap_array = []
shell_array = []
N_array = []

with open("quick_sorts.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        merge_array.append(float(stroke[2]))
        heap_array.append(float(stroke[3]))
        shell_array.append(float(stroke[4]))
        N_array.append(int(stroke[1]))

with open("quick_sorts_qs.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        quick_array.append(float(stroke[2]))

merge_np_array = np.array(merge_array)
quick_np_array = np.array(quick_array)
heap_np_array = np.array(heap_array)
shell_np_array = np.array(shell_array)
N_np_array = np.array(N_array)*np.log(np.array(N_array))

fig, ax = plt.subplots(nrows=2, ncols=3, figsize=(10, 8))
ax[1, 2].remove()

markers = {0: "s", 1: "o", 2: "x"}
labels = {0: "random", 1: "ordered", 2: "reversed"}

for i in range(3):
    ax[0, 0].plot(N_np_array[0:10], merge_np_array[10*i:10*(i + 1)], color='blue', marker=markers[i], label=labels[i])
    ax[0, 1].plot(N_np_array[0:7], quick_np_array[7*i:7*(i + 1)], color='red', marker=markers[i], label=labels[i])
    ax[1, 0].plot(N_np_array[0:10], heap_np_array[10*i:10*(i + 1)], color='green', marker=markers[i], label=labels[i])
    ax[1, 1].plot(N_np_array[0:10], shell_np_array[10*i:10*(i + 1)], color='purple', marker=markers[i], label=labels[i])

ax[0, 0].set_title('Merge sort')
ax[0, 1].set_title('Quick sort')
ax[1, 0].set_title('Heap sort')
ax[1, 1].set_title('Shell sort')

ax[0, 2].plot(N_np_array[0:10], merge_np_array[0:10], color='blue', marker="s", label="merge (random)")
ax[0, 2].plot(N_np_array[0:7], quick_np_array[0:7], color='red', marker="s", label="quick (random)")
ax[0, 2].plot(N_np_array[0:10], heap_np_array[0:10], color='green', marker="s", label="heap (random)")
ax[0, 2].plot(N_np_array[0:10], shell_np_array[0:10], color='purple', marker="s", label="shell (random)")
ax[0, 2].set_title('Сравнение сортировок')

fig.supxlabel('NlnN')
fig.supylabel('T')
ax[0, 0].legend()
ax[0, 1].legend()
ax[1, 0].legend()
ax[1, 1].legend()
ax[0, 2].legend()

fig.suptitle('Быстрые сортировки -O0', fontsize=16, fontweight='bold')
plt.tight_layout()
fig.savefig('quick_sorts.png')
plt.show()