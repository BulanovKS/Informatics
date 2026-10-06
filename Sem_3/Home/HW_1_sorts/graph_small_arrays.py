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

with open("small_arrays.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        # [Тип данных, T]
        bubble_array.append(float(stroke[1]))
        insertion_array.append(float(stroke[2]))
        selection_array.append(float(stroke[3]))
        merge_array.append(float(stroke[4]))
        quick_array.append(float(stroke[5]))
        heap_array.append(float(stroke[6]))
        shell_array.append(float(stroke[7]))
        N_array.append(int(stroke[0]))


bubble_np_array = np.array(bubble_array)
insertion_np_array = np.array(insertion_array)
selection_np_array = np.array(selection_array)
merge_np_array = np.array(merge_array)
quick_np_array = np.array(quick_array)
heap_np_array = np.array(heap_array)
shell_np_array = np.array(shell_array)

N_np_array = np.array(N_array)

plt.plot(N_np_array, bubble_np_array, color='black', marker="d", label="bubble (random)")
plt.plot(N_np_array, insertion_np_array, color='orange', marker=">", label="insertion (random)")
plt.plot(N_np_array, selection_np_array, color='purple', marker="*", label="selection (random)")

plt.plot(N_np_array, merge_np_array, color='blue', marker="s", label="merge (random)")
plt.plot(N_np_array, quick_np_array, color='red', marker="o", label="quick (random)")
plt.plot(N_np_array, heap_np_array, color='green', marker="x", label="heap (random)")
plt.plot(N_np_array, shell_np_array, color='pink', marker="+", label="shell (random)")

plt.xlabel('N')
plt.ylabel('T')
plt.legend()

plt.title('Сортировки на малых массивах -O0', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('small_arrays.png')
plt.show()