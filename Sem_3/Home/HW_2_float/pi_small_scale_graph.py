import numpy as np
import matplotlib.pyplot as plt

l_array = [] # Лейбниц
n_array = [] # Нилакант
w_array = [] # Валлис
b_array = [] # Бэйли-Боруэйн-Плафф
u_array = [] # Безымянный

N_array = []

with open("pi_csv.csv", "r", encoding="utf_8") as file:
    next(file)
    for line in file:
        stroke = list(map(str, line.split(",")))
        l_array.append(float(stroke[1]))
        n_array.append(float(stroke[2]))
        w_array.append(float(stroke[3]))
        b_array.append(float(stroke[4]))
        u_array.append(float(stroke[5]))
        N_array.append(int(stroke[0]))

l_np_array = np.array(l_array)
n_np_arrya = np.array(n_array)
w_np_arrya = np.array(w_array)
b_np_arrya = np.array(b_array)
u_np_arrya = np.array(u_array)

N_np_array = np.array(N_array)

t = 1 # шаг между количеством итераций равен 10*t, t >= 1
h = 60 # крайняя точка оси абсцисс
plt.plot(N_np_array[:h:t], l_np_array[:h:t], color='green', marker="o", ms = 1, label="Leibniz")
plt.plot(N_np_array[:h:t], n_np_arrya[:h:t], color='orange', marker="s", ms = 1, label="Nilakantha")
plt.plot(N_np_array[:h:t], w_np_arrya[:h:t], color='purple', marker="o", ms = 1, label="Wallis")
plt.plot(N_np_array[:h:t], b_np_arrya[:h:t], color='blue', marker="o", ms = 1, label="BBP")
plt.plot(N_np_array[:h:t], u_np_arrya[:h:t], color='red', marker="o", ms = 1, label="Untitled")

plt.axhline(y=3.141592653589793, xmin=0, xmax=1000, color='black', alpha = 0.5)

plt.xlabel('N')
plt.ylabel('Value')
plt.legend()

plt.title("Сравнение иттерационных формул вычисления числа $\\pi$", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('pi_small_scale.png')
plt.show()