# Task A

"""
Список, с которым оперируем, как со стэком.
Если скобка открывающая, то добавляем в стэк.
Если скобка закрывающая, то смотрим, что лежит на вершине стэка: если на вершине лежит соответсвующая скобка, то удаляем ее, если не соответсвующая, то пишем "no"
Дальше следуем аналогично.
Если в конце стэк не пустой, или было выведено "no", то последовательность неправильная.

stroke_list = list(input())
stroke_dict = {"{": "}", "[": "]", "(": ")"}
stack = []

for i in range(0, len(stroke_list)):
    print(stack)
    if stroke_list[i] in stroke_dict.keys():
        stack.extend(stroke_list[i])
    else:
        if len(stack) == 0: continue
        elif len(stack) > 0 and stroke_dict.get(stack[-1]) == stroke_list[i]:
            stack.pop()

if len(stack) == 0: print("Yes")
else: print("No")
"""

# Task B

"""
Проставление точек на правых концах (отрезков), которые находятся левее всего.
Проверка на попадание в другие отрезки: левая граница следующего отрезка левее последней точки, тогда выкидываем отрезок.

Отрезки:

  --     ------                -*     ------
-------    --------   ->     -------    --------
    ---------                     --------*

Итого: две точки

Перед этим надо отсортировать правые концы отрезков функцией sort(key = lambda x: x[1])
[Можно задавать функции в одну строчку через лямбда-функцию: lambda <arg1>, <arg2>, ...: <function>.]



N = int(input())
seg = [list(map(int, input().split())) for i in range(N)]
detectors = 0

while len(seg) > 0:
    seg.sort(key = lambda x: x[1])
    detectors += 1
    current_detector = seg[0][1]
    seg.sort(key = lambda x: x[0])
    i = 0
    while i + 1 < len(seg) and seg[i + 1][0] <= current_detector :
        i += 1
    del seg[:i + 1]

print(detectors)


N = int(input())
segments = [list(map(int, input().split())) for i in range(N)]
segments.sort(key = lambda x: x[1])

current_detector = segments[0][1]
detectors = 1

for i in segments:
    if current_detector < i[0]:
        detectors += 1
        current_detector = i[1]

print(detectors)
"""

# Task C

"""
K = input()
n = len(s)
for i in range(n):
    for j in range(i+1, n):
        if s[i] > s[j]:
            count += 1
            
Для каждой строки считаем метрику, потом сортируем строки по возрастанию метрики.

K = int(input())
for i in range(K):
    n, m = map(int, input().split())
    strokes = [input() for j in range(m)]

    output_dict = {}
    output_list = []

    for k in strokes:
        replacements = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if k[i] > k[j]:
                    replacements += 1
        output_dict[k] = replacements

    while len(output_dict) > 0:
        replacements_minimum = 1251
        for l in output_dict:
            if output_dict[l] < replacements_minimum:
                replacements_minimum = output_dict[l]
                needed_key = l
        output_list.append(needed_key)
        del output_dict[needed_key]

    output_list.append("")
    for i in range(len(output_list)):
        print(output_list[i])
"""

# Task D

"""
Используем: 
1) сортированный список задач по дедлайнам
2) суммарное время выполнения задач (таймер) T 
3) максимальная куча, в которой лежат время выполнения i-той задачи, добавляя элементы в кучу, сортируя их по дедлайнам

Добавляем в кучу i-тую задачу по отсортированному списку дедлайнов
Добавляя в кучу, обновляем T += ti
Решаем i-тую задачу: если в корне кучи лежит задание, из-за которого не успеваем к текущему дедлайну, то выкидываем корень из кучи
Возвращаем высоту кучи

import heapq
N = int(input())
td = [list(map(int, input().split())) for i in range(N)]
td.sort(key = lambda x: x[1])

timer = 0
time_heap = []
heapq.heapify(time_heap)

for i in range(len(td)):
    if td[i][0] <= td[i][1]:
        heapq.heappush(time_heap, -td[i][0])
        timer += td[i][0]
        if timer > td[i][1]: timer -= -heapq.heappop(time_heap)
        else: continue
    else: continue

print(len(time_heap))
"""

# Task E

"""
Создать словарь: в ключах лежат отсортированное множество букв, из которых состоят слова, в значениях - множество слов, состоящих из них.
Пример: {aet: [ate, eat, tea]}

words = list(input().split())
letters_dict = {}

for i in words:
    letters = "".join(sorted(i))
    if letters not in letters_dict: letters_dict[letters] = []
    letters_dict[letters].append(i)
    letters_dict[letters].sort()

words_list = list(letters_dict.values())
words_list.sort(key = lambda x: len(x))
output_words_list = []

k = 0
for i in range(len(words_list)):
    if len(words_list[i]) > 1:
        output_words_list = words_list[i] + output_words_list
    else:
        output_words_list.extend(words_list[i])
        k += 1

output_words_list[-k:] = sorted(output_words_list[-k:])
print(*output_words_list)
"""

# Task F

"""
Создаем минимальную и максимальную, отличающихся по высоте не больше, чем на 1.
Медиана либо является средним арифметическим корней куч (при одинаковых размерах куч), либо находится в куче с большей высотой.
Текущую медиану храним в памяти.
Добавляем элемент в кучу: 
а) если меньше или равно медианы, то в максимальную кучу
б) если больше медианы, то в минимальную кучу
в) если высоты куч отличаются больше, чем на 1, то перекладываем корень из большей кучи в меньшую
"""

# Task G

"""
Бинарное дерево поиска, операция split
"""