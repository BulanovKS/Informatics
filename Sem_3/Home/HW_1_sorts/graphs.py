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
        # [Тип оптимизации, T]
        bubble_array.append([int(stroke[0]), float(stroke[2])])
        insertion_array.append([int(stroke[0]), float(stroke[3])])
        selection_array.append([int(stroke[0]), float(stroke[4])])
        N_array.append(int(stroke[1])) #ПОВТОРЯЮЩИЕСЯ ЗНАЧЕНИЯ В СПИСКЕ

bubble_np_array = np.array(bubble_array)
insertion_np_array = np.array(insertion_array)
selection_np_array = np.array(selection_array)
N_np_array = np.array(N_array)

print(bubble_array, "\n", N_array)
