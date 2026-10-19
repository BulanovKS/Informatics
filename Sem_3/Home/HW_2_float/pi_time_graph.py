import numpy as np
import matplotlib.pyplot as plt

l_array = [] # Лейбниц
n_array = [] # Нилакант
w_array = [] # Валлис
b_array = [] # Бэйли-Боруэйн-Плафф
u_array = [] # Безымянный

N_array = []

with open("pi_time_csv.csv", "r", encoding="utf_8") as file:
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
n_np_array = np.array(n_array)
w_np_array = np.array(w_array)
b_np_array = np.array(b_array)
u_np_array = np.array(u_array)

N_np_array = np.array(N_array)

ymin, ymax = plt.ylim()
plt.yticks(np.arange(ymin, ymax, 0.005))

plt.plot(N_np_array, l_np_array, color='green', marker="o", ms = 1,  label="Leibniz")
plt.plot(N_np_array, n_np_array, color='orange', marker="o", ms = 1,  label="Nilakantha")
plt.plot(N_np_array, w_np_array, color='purple', marker="o", ms = 1,  label="Wallis")
plt.plot(N_np_array, b_np_array, color='blue', marker="o", ms = 1,  label="BBP")
plt.plot(N_np_array, u_np_array, color='red', marker="o", ms = 1,  label="Untitled")

l_coef = np.polyfit(N_np_array, l_np_array, 1)
n_coef = np.polyfit(N_np_array, n_np_array, 1)
w_coef = np.polyfit(N_np_array, w_np_array, 1)
b_coef = np.polyfit(N_np_array, b_np_array, 1)
u_coef = np.polyfit(N_np_array, u_np_array, 1)

l_appr = np.polyval(l_coef, N_np_array)
n_appr = np.polyval(n_coef, N_np_array) 
w_appr = np.polyval(w_coef, N_np_array) 
b_appr = np.polyval(b_coef, N_np_array) 
u_appr = np.polyval(u_coef, N_np_array) 

plt.plot(N_np_array, l_appr, color='green', marker="o", ms = 1, alpha = 0.5)
plt.plot(N_np_array, n_appr, color='orange', marker="o", ms = 1, alpha = 0.5)
plt.plot(N_np_array, w_appr, color='purple', marker="o", ms = 1, alpha = 0.5)
plt.plot(N_np_array, b_appr, color='blue', marker="o", ms = 1, alpha = 0.5)
plt.plot(N_np_array, u_appr, color='red', marker="o", ms = 1, alpha = 0.5)

plt.xlabel('Точность (кол-во совпадающих знаков после запятой)')
plt.ylabel('Время работы алгоритмов (за 1,000,000 повторений)')
plt.legend()

plt.title("Сравнение иттерационных формул вычисления числа $\\pi$", fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('pi_time.png')
plt.show()