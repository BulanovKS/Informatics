#from Seminar_06_02_26 import read_graph_as_list
import time

#TODO A DFS
"""
def read_graph_as_list(N, M): # список смежности, N вершин, M ребер, индексация вершин с 1
    adj_dict = {}
    for i in range(M):
        e1, e2 = list(map(int, input().split()))
        adj_dict.setdefault(e1, [])
        adj_dict.setdefault(e2, [])
        adj_dict[e1].append(e2)

    return adj_dict

def dfs(graph, v, prev):
    stack = [v]
    while stack:
        node = stack.pop()
        if node not in prev:
            prev.add(node)
        unvisited_neighbors = set(graph[node]) - prev
        stack.extend(unvisited_neighbors)
    return prev

n, m = map(int, input().split())
G = read_graph_as_list(m, n)

prev = set()

dfs(G, 1, prev)

print(len(prev))

for _ in sorted(prev):
    print(_)
"""
"""
6 11
1 4
2 3
4 5
2 5
4 7
4 10

5 5
1 2
1 4
2 4
2 4
3 4
"""
# TODO B DFS с расчетом зарплаты на обратном ходу
"""
def read_graph(N):
    adj_dict = {(_ + 1): [] for _ in range(N) }
    for i in range(1, N + 1):
        stroke = input()
        k = 0
        while k <= len(stroke):
            position = stroke.find("Y", k)
            if position == -1:
                break
            else:
                k = position + 1
                adj_dict[i].append(k)
    return adj_dict

def dfs(graph, v, visited, score):
    visited[v] = 'gray'

    for u in graph[v]:
        if visited[u] == 'white':
            dfs(graph, u, visited, score)
        score[v] += score[u]

    visited[v] = 'black'

n = int(input())
G = read_graph(n)

visited = ['white' for _ in range(n + 1)]
score = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    if not G.get(i):
        score[i] = 1

for i in range(1, n + 1):
    if visited[i] == 'white':
        dfs(G, i, visited, score)

print(sum(score))
"""
"""
6
NNNNNN
YNYNNY
YNNNNY
NNNNNN
YNYNNN
YNNYNN
"""
#TODO C Граф, где вершины - буквы, ребра - перестановка (от того, что было, к тому, что стало). Цикл длины N соответствует N-1 перестановкам: цикл длины 2 - 1 перестановка, цикл длины 3 - две перестановки
"""
def read_graph_as_list(): # список смежности, N вершин, M ребер, индексация вершин с 1
    adj_dict = {'A': [], 'C': [], 'G': [], 'T': []}
    stroke1 = list(input())
    stroke2 = list(input())
    for i in range(len(stroke1)):
        adj_dict[stroke1[i]].append(stroke2[i])

    return adj_dict

def connected_components(graph): # определяет компоненты связанности в графе, graph - список смежности
    visited = set()
    components = []

    vertices = ['A', 'C', 'G', 'T']

    for start in vertices:
        if start in visited:
            continue

        # Новая компонента
        comp = []
        stack = [start]
        visited.add(start)

        while stack:
            u = stack.pop()
            comp.append(u)

            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

        components.append(comp)

    return components

def find_max_cycle(graph, start):
    colors = {_: "white" for _ in graph.keys()}
    colors[start] = "gray"
    stack = [(None, start)]
    k = 0
    while stack:
        (prev, node) = stack.pop()
        for neighbor in graph[node]:
            if neighbor == prev and len(graph) == 2:
                return 1
            if neighbor == prev and k <= 1:
                pass
            elif colors[neighbor] == "gray" and node == start:
                if k - 1 < 0: return 0
                elif k == 1 : return 1
                else: return k-1
            else:
                colors[neighbor] = "gray"
                stack.append((node, neighbor))
                k += 1
    return 0

G = read_graph_as_list()
count = 0
counter = []

CC = connected_components(G)

for cc in CC:
    graph = {}
    counter = []
    for v in cc:
        graph.setdefault(v, G[v])
    for i in cc:
        counter.append(find_max_cycle(graph, i))
    print(counter)
    count += max(counter)

print(G, CC, count)
"""
#TODO D Поменять знаки неравенств и весов. Построить ориентированный по знаку неравенства и взвешенный по суммарному росту граф. Найти цикл отрицательной стоимости (алг. Флоида-Уойршелла, на диагонали отрицательная стоимость)

"""
def fordbellman(G, N):
    dist = [0]*(N+1)
    for k in range(N):
        updated = False
        for i, j, w in array_:
            if dist[j] > dist[i] + w:
                dist[j] = dist[i] + w
                updated = True
                if k == N-1:
                    return True
        if not updated:
           break
    return False

if fordbellman(array_, N):
    print('YES')
else:
    print('NO')
"""
"""
N, M = map(int, input().split())
array_ = []

for i in range(M):
    group = list(input().split())
    l = int(group[0])
    r = int(group[1])
    k = int(group[2])
    sign = group[3]
    if sign == '<=':
        array_.append((l, r, k))
    else:
        array_.append((r, l, -k))

def BelmanFord(G, s): # решается проблема отриц. ребер и циклов, G - список смежности, нумерация с 1
    V = len(G) + 1
    dist = [float('inf') for i in range(V)]
    dist[s] = 0

    for k in range(1,V):
        updated = False
        for v, u, weight in G:
            if dist[u] > dist[v] + weight:
                dist[u] = dist[v] + weight
                updated = True
                if k == N - 1:
                    return True

        if not updated:
            break

    return False

if BelmanFord(array_, N):
    print('YES')
else:
    print('NO')
"""

#TODO E Посчитать кол-во компонент связанности, в которых нет цикла
"""
def read_graph_as_list(M): # список смежности, N вершин, M ребер, индексация вершин с 1
    adj_dict = {}
    for i in range(M):
        e1, e2 = list(map(int, input().split()))
        adj_dict.setdefault(e1, [])
        adj_dict.setdefault(e2, [])
        adj_dict[e1].append(e2)
        adj_dict[e2].append(e1)

    return adj_dict

def connected_components(graph): # определяет компоненты связанности в графе, graph - список смежности
    visited = set()
    components = []

    vertices = list(range(1, len(graph) + 1))

    for start in vertices:
        if start in visited:
            continue

        # Новая компонента
        comp = []
        stack = [start]
        visited.add(start)

        while stack:
            u = stack.pop()
            comp.append(u)

            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)

        components.append(comp)

    return components

def find_cycle(n, graph, start):
    colors = {_: "white" for _ in graph.keys()}
    colors[start] = "gray"
    stack = [(None, start)]
    while stack:
        (prev, node) = stack.pop()
        for neighbor in graph[node]:
            if neighbor == prev:
                pass
            elif colors[neighbor] == "gray":
                return True
            else:
                colors[neighbor] = "gray"
                stack.append((node, neighbor))
    return False

n, m = map(int, input().split())
G = read_graph_as_list(m)
for i in range(1, n + 1):
    if i not in G: G.setdefault(i, [])
count = 0

CC = connected_components(G)

for cc in CC:
    graph = {}
    for v in cc:
        graph.setdefault(v, G[v])
    if find_cycle(n, graph, cc[0]):
        count += 1

print(len(CC) - count)
"""
#TODO F Система непересекающихся множеств из вершин. Начинаем идти в обратном порядке: добавляем ребра (вместо cut - union), и определяем результат ask

def find(graph, k):
    if graph[k - 1] != k:
        graph[k - 1] = find(graph, graph[k - 1])
    return graph[k - 1]


def union(graph1, graph2, x, y):
    x = find(graph1, x)
    y = find(graph1, y)
    if x == y:
        return
    if graph2[x - 1] == graph1[y - 1]:
        graph2[x - 1] += 1
    if graph2[x - 1] < graph2[y - 1]:
        graph1[x - 1] = y
    else:
        graph1[y - 1] = x


n, m, k = map(int, input().split())
for _ in range(m): input()

actions = [input() for _ in range(k)]
actions = actions[::-1]
graph = [i for i in range(1, n + 1)]
size = [0] * n
answers = []

for operation in actions:
    action, x, y = operation.split()
    x, y = int(x), int(y)

    if action == 'ask':
        if find(graph, x) == find(graph, y):
            answers.append('YES')
        else:
            answers.append('NO')

    if action == 'cut':
        union(graph, size, x, y)

answers = answers[::-1]
print('\n'.join(answers))
