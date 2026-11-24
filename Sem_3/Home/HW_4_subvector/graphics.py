import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Настройка стиля графиков
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

def plot_task0():
    """График зависимости capacity от size для std::vector."""
    try:
        df = pd.read_csv('csv_task0.csv')
    except FileNotFoundError:
        print("Файл csv_task0.csv не найден. Пропускаем task0.")
        return

    plt.figure()
    plt.plot(df['size'], df['capacity'], label='std::vector', color='blue')
    plt.xlabel('size (количество элементов)')
    plt.ylabel('capacity (ёмкость)')
    plt.title('Зависимость capacity от size для std::vector')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('task0_capacity_vs_size.png', dpi=150)
    plt.show()

    # Дополнительно: логарифмический масштаб, чтобы увидеть экспоненциальный рост
    plt.figure()
    plt.loglog(df['size'], df['capacity'], label='std::vector', color='blue')
    plt.xlabel('size (лог. шкала)')
    plt.ylabel('capacity (лог. шкала)')
    plt.title('Зависимость capacity от size (лог-лог)')
    plt.legend()
    plt.grid(True, which='both', ls='--')
    plt.tight_layout()
    plt.savefig('task0_capacity_vs_size_loglog.png', dpi=150)
    plt.show()

def plot_task1():
    """Сравнение стратегий роста subvector и std::vector."""
    try:
        df = pd.read_csv('csv_task1.csv')
    except FileNotFoundError:
        print("Файл csv_task1.csv не найден. Пропускаем task1.")
        return

    # Заменяем -1 на NaN, чтобы не отображать прерванные замеры
    df.replace(-1.0, np.nan, inplace=True)

    plt.figure()
    plt.plot(df['n'], df['plus_10'], 'o-', label='+10')
    plt.plot(df['n'], df['plus_100'], 's-', label='+100')
    plt.plot(df['n'], df['mul_1_5'], '^-', label='*1.5')
    plt.plot(df['n'], df['mul_2'], 'd-', label='*2')
    plt.plot(df['n'], df['stdvector'], 'x-', label='std::vector', linewidth=2, markersize=8)

    plt.xlabel('n (количество добавляемых элементов)')
    plt.ylabel('Время заполнения, сек')
    plt.title('Сравнение стратегий роста capacity')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('task1_strategies_comparison.png', dpi=150)
    plt.show()

    # Анализ: для каждого n определим лучшую стратегию (кроме std::vector)
    # и сравним с std::vector
    print("\n--- Анализ task1 ---")
    for i, row in df.iterrows():
        n = int(row['n'])
        times = {
            '+10': row['plus_10'],
            '+100': row['plus_100'],
            '*1.5': row['mul_1_5'],
            '*2': row['mul_2'],
            'std::vector': row['stdvector']
        }
        # Убираем NaN
        times = {k: v for k, v in times.items() if not pd.isna(v)}
        if not times:
            continue
        best_sub = min((k, v) for k, v in times.items() if k != 'std::vector')
        std_time = times.get('std::vector', None)
        print(f"n={n:>9}: лучшая стратегия subvector: {best_sub[0]:>4} ({best_sub[1]:.4f} с), "
              f"std::vector: {std_time:.4f} с" if std_time else "")

    # Вывод: std::vector обычно использует стратегию удвоения (×2) или ×1.5,
    # что видно по времени: оно близко к *2 или *1.5.
    print("Обычно std::vector использует стратегию удвоения (×2) или ×1.5, "
          "поэтому его время близко к соответствующей стратегии subvector.")

def plot_task2a():
    """Зависимость времени от множителя capacity."""
    try:
        df = pd.read_csv('csv_task2a.csv')
    except FileNotFoundError:
        print("Файл csv_task2a.csv не найден. Пропускаем task2a.")
        return

    plt.figure()
    plt.plot(df['multiplier'], df['time'], 'o-', color='green')
    plt.xlabel('Множитель capacity (grow_param при grow_type=1)')
    plt.ylabel('Время заполнения, сек')
    plt.title('Зависимость времени от множителя capacity (n=5 млн)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('task2a_multiplier_vs_time.png', dpi=150)
    plt.show()

    # Поиск оптимального множителя (минимум времени)
    min_idx = df['time'].idxmin()
    opt_mult = df.loc[min_idx, 'multiplier']
    opt_time = df.loc[min_idx, 'time']
    print(f"\n--- Анализ task2a ---")
    print(f"Оптимальный множитель capacity: {opt_mult:.2f} (время {opt_time:.4f} с)")
    print("Слишком маленький множитель приводит к частым перевыделениям памяти,")
    print("слишком большой — к избыточному выделению и копированию больших объёмов.")

def plot_task2b():
    """Зависимость времени от константы прибавления к capacity."""
    try:
        df = pd.read_csv('csv_task2b.csv')
    except FileNotFoundError:
        print("Файл csv_task2b.csv не найден. Пропускаем task2b.")
        return

    plt.figure()
    # Логарифмическая шкала по оси X, так как значения от 10 до 500000
    plt.semilogx(df['additive'], df['time'], 's-', color='purple')
    plt.xlabel('Константа прибавления к capacity (grow_param при grow_type=0)')
    plt.ylabel('Время заполнения, сек')
    plt.title('Зависимость времени от константы прибавления (n=1 млн)')
    plt.grid(True, which='both', ls='--')
    plt.tight_layout()
    plt.savefig('task2b_additive_vs_time.png', dpi=150)
    plt.show()

    # Поиск оптимальной константы (минимум времени)
    min_idx = df['time'].idxmin()
    opt_add = df.loc[min_idx, 'additive']
    opt_time = df.loc[min_idx, 'time']
    print(f"\n--- Анализ task2b ---")
    print(f"Оптимальная константа прибавления: {opt_add} (время {opt_time:.4f} с)")
    print("Маленькие константы вызывают много перевыделений, большие — перерасход памяти")
    print("и копирование больших блоков, что также увеличивает время.")

if __name__ == '__main__':
    plot_task0()
    plot_task1()
    plot_task2a()
    plot_task2b()