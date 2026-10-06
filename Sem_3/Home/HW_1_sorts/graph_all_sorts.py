import numpy as np
import matplotlib.pyplot as plt

bubble_array = []
insertion_array = []
selection_array = []

merge_array = []
quick_array = []
heap_array = []
shell_array = []

N_array = []

with open("slow_sorts.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array.append(float(stroke[2]))
        insertion_array.append(float(stroke[3]))
        selection_array.append(float(stroke[4]))

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

bubble_np_array = np.array(bubble_array)
insertion_np_array = np.array(insertion_array)
selection_np_array = np.array(selection_array)

merge_np_array = np.array(merge_array)
quick_np_array = np.array(quick_array)
heap_np_array = np.array(heap_array)
shell_np_array = np.array(shell_array)

N_np_array = np.array(N_array)

plt.plot(N_np_array[0:10], bubble_np_array[0:10], color='black', marker="s", label="bubble (random)")
plt.plot(N_np_array[0:10], insertion_np_array[0:10], color='orange', marker="s", label="insertion (random)")
plt.plot(N_np_array[0:10], selection_np_array[0:10], color='purple', marker="s", label="selection (random)")

plt.plot(N_np_array[0:10], merge_np_array[0:10], color='blue', marker="s", label="merge (random)")
plt.plot(N_np_array[0:7], quick_np_array[0:7], color='red', marker="o", label="quick (random)")
plt.plot(N_np_array[0:10], heap_np_array[0:10], color='green', marker="x", label="heap (random)")
plt.plot(N_np_array[0:10], shell_np_array[0:10], color='pink', marker="+", label="shell (random)")

plt.xlabel('N')
plt.ylabel('T')
plt.legend()

plt.title('Сравнение всех сортировок -O0', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('all_sorts.png')
plt.show()