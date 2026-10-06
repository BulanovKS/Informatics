import numpy as np
import matplotlib.pyplot as plt

bubble_array_o0 = []
bubble_array_o1 = []
bubble_array_o2 = []
bubble_array_o3 = []

insertion_array_o0 = []
insertion_array_o1 = []
insertion_array_o2 = []
insertion_array_o3 = []

selection_array_o0 = []
selection_array_o1 = []
selection_array_o2 = []
selection_array_o3 = []
N_array = []

with open("slow_sorts.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array_o0.append(float(stroke[2]))
        insertion_array_o0.append(float(stroke[3]))
        selection_array_o0.append(float(stroke[4]))
        N_array.append(int(stroke[1]))

with open("slow_sorts_o1.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array_o1.append(float(stroke[2]))
        insertion_array_o1.append(float(stroke[3]))
        selection_array_o1.append(float(stroke[4]))       

with open("slow_sorts_o2.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array_o2.append(float(stroke[2]))
        insertion_array_o2.append(float(stroke[3]))
        selection_array_o2.append(float(stroke[4]))

with open("slow_sorts_o3.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array_o3.append(float(stroke[2]))
        insertion_array_o3.append(float(stroke[3]))
        selection_array_o3.append(float(stroke[4])) 

bubble_np_array_o0 = np.log(np.array(bubble_array_o0))
bubble_np_array_o1 = np.log(np.array(bubble_array_o1))
bubble_np_array_o2 = np.log(np.array(bubble_array_o2))
bubble_np_array_o3 = np.log(np.array(bubble_array_o3))

insertion_np_array_o0 = np.log(np.array(insertion_array_o0))
insertion_np_array_o1 = np.log(np.array(insertion_array_o1))
insertion_np_array_o2 = np.log(np.array(insertion_array_o2))
insertion_np_array_o3 = np.log(np.array(insertion_array_o3))

selection_np_array_o0 = np.log(np.array(selection_array_o0))
selection_np_array_o1 = np.log(np.array(selection_array_o1))
selection_np_array_o2 = np.log(np.array(selection_array_o2))
selection_np_array_o3 = np.log(np.array(selection_array_o3))

N_np_array = np.log(np.array(N_array))

fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(10, 8))

markers = {0: "s", 1: "o", 2: "x", 3: "+"}

ax[0, 0].plot(N_np_array[0:10], bubble_np_array_o0[0:10], color='blue', marker=markers[0], label="o0 (random)")
ax[0, 0].plot(N_np_array[0:10], bubble_np_array_o1[0:10], color='blue', marker=markers[1], label="o1 (random)")
ax[0, 0].plot(N_np_array[0:10], bubble_np_array_o2[0:10], color='blue', marker=markers[2], label="o2 (random)")
ax[0, 0].plot(N_np_array[0:10], bubble_np_array_o3[0:10], color='blue', marker=markers[3], label="o3 (random)")

ax[1, 0].plot(N_np_array[0:10], bubble_np_array_o0[10:20], color='blue', marker=markers[0], label="o0 (ordered)")
ax[1, 0].plot(N_np_array[0:10], bubble_np_array_o1[10:20], color='blue', marker=markers[1], label="o1 (ordered)")
ax[1, 0].plot(N_np_array[0:10], bubble_np_array_o2[10:20], color='blue', marker=markers[2], label="o2 (ordered)")
ax[1, 0].plot(N_np_array[0:10], bubble_np_array_o3[10:20], color='blue', marker=markers[3], label="o3 (ordered)")

ax[2, 0].plot(N_np_array[0:10], bubble_np_array_o0[20:30], color='blue', marker=markers[0], label="o0 (reversed)")
ax[2, 0].plot(N_np_array[0:10], bubble_np_array_o1[20:30], color='blue', marker=markers[1], label="o1 (reversed)")
ax[2, 0].plot(N_np_array[0:10], bubble_np_array_o2[20:30], color='blue', marker=markers[2], label="o2 (reversed)")
ax[2, 0].plot(N_np_array[0:10], bubble_np_array_o3[20:30], color='blue', marker=markers[3], label="o3 (reversed)")

ax[0, 1].plot(N_np_array[0:10], insertion_np_array_o0[0:10], color='red', marker=markers[0], label="o0 (random)")
ax[0, 1].plot(N_np_array[0:10], insertion_np_array_o1[0:10], color='red', marker=markers[1], label="o1 (random)")
ax[0, 1].plot(N_np_array[0:10], insertion_np_array_o2[0:10], color='red', marker=markers[2], label="o2 (random)")
ax[0, 1].plot(N_np_array[0:10], insertion_np_array_o3[0:10], color='red', marker=markers[3], label="o3 (random)")

ax[1, 1].plot(N_np_array[0:10], insertion_np_array_o0[10:20], color='red', marker=markers[0], label="o0 (ordered)")
ax[1, 1].plot(N_np_array[0:10], insertion_np_array_o1[10:20], color='red', marker=markers[1], label="o1 (ordered)")
ax[1, 1].plot(N_np_array[0:10], insertion_np_array_o2[10:20], color='red', marker=markers[2], label="o2 (ordered)")
ax[1, 1].plot(N_np_array[0:10], insertion_np_array_o3[10:20], color='red', marker=markers[3], label="o3 (ordered)")

ax[2, 1].plot(N_np_array[0:10], insertion_np_array_o0[20:30], color='red', marker=markers[0], label="o0 (reversed)")
ax[2, 1].plot(N_np_array[0:10], insertion_np_array_o1[20:30], color='red', marker=markers[1], label="o1 (reversed)")
ax[2, 1].plot(N_np_array[0:10], insertion_np_array_o2[20:30], color='red', marker=markers[2], label="o2 (reversed)")
ax[2, 1].plot(N_np_array[0:10], insertion_np_array_o3[20:30], color='red', marker=markers[3], label="o3 (reversed)")

ax[0, 2].plot(N_np_array[0:10], selection_np_array_o0[0:10], color='green', marker=markers[0], label="o0 (random)")
ax[0, 2].plot(N_np_array[0:10], selection_np_array_o1[0:10], color='green', marker=markers[1], label="o1 (random)")
ax[0, 2].plot(N_np_array[0:10], selection_np_array_o2[0:10], color='green', marker=markers[2], label="o2 (random)")
ax[0, 2].plot(N_np_array[0:10], selection_np_array_o3[0:10], color='green', marker=markers[3], label="o3 (random)")

ax[1, 2].plot(N_np_array[0:10], selection_np_array_o0[10:20], color='green', marker=markers[0], label="o0 (ordered)")
ax[1, 2].plot(N_np_array[0:10], selection_np_array_o1[10:20], color='green', marker=markers[1], label="o1 (ordered)")
ax[1, 2].plot(N_np_array[0:10], selection_np_array_o2[10:20], color='green', marker=markers[2], label="o2 (ordered)")
ax[1, 2].plot(N_np_array[0:10], selection_np_array_o3[10:20], color='green', marker=markers[3], label="o3 (ordered)")

ax[2, 2].plot(N_np_array[0:10], selection_np_array_o0[20:30], color='green', marker=markers[0], label="o0 (reversed)")
ax[2, 2].plot(N_np_array[0:10], selection_np_array_o1[20:30], color='green', marker=markers[1], label="o1 (reversed)")
ax[2, 2].plot(N_np_array[0:10], selection_np_array_o2[20:30], color='green', marker=markers[2], label="o2 (reversed)")
ax[2, 2].plot(N_np_array[0:10], selection_np_array_o3[20:30], color='green', marker=markers[3], label="o3 (reversed)")

ax[0, 0].set_title('Bubble sort')
ax[0, 1].set_title('Insertion sort')
ax[0, 2].set_title('Selection sort')

fig.supxlabel('lnN')
fig.supylabel('lnT')

for i in range(3):
    for j in range(3):
        ax[i, j].legend()


fig.suptitle('Медленные сортировки и их оптимизация', fontsize=16, fontweight='bold')
plt.tight_layout()
fig.savefig('optimisation.png')
plt.show()