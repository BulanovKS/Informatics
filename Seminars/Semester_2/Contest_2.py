#TODO A
#Граф: вершины - города, ребра - задержки. Надо перебрать вершины, запуская алгоритм Дейкстры (попробовать и на куче и на массиве), находя город, где суммарная задержка до всех городов должна быть минимальна

"""
import heapq

def read_graph_as_edges_list(N): # список ребер, n ребер в графе, индексация вершин с 1
    edges = []
    for i in range(N):
        e = list(map(int,input().split()))
        edges.append(e)
    return edges

def read_graph_as_list(N, M): # список смежности, N вершин, M ребер, индексация вершин с 1
    edges = read_graph_as_edges_list(M)
    adj_dict = {(i + 1): [] for i in range(N)}
    for e in edges:
        adj_dict[e[0]].append((e[1], e[2]))
        adj_dict[e[1]].append((e[0], e[2]))
    return adj_dict

def dijkstra(G, s, n): # реализация на кучах
    # G - граф, представленный списком смежности, индексация с 1
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    pq = [(0, s)] # (distance, node)

    while pq:
        cur_dist, v = heapq.heappop(pq)

        if cur_dist > dist[v]:
            continue

        for to, weight in G.get(v, []):
            new_dist = cur_dist + weight

            if new_dist < dist[to]:
                dist[to] = new_dist
                heapq.heappush(pq, (new_dist, to))

    return dist

n, m, k = map(int, input().split())
c_list = list(map(int, input().split()))

graph = read_graph_as_list(n, m)

summ = 0
answer = [n + 1, float('inf')]
dist = {}

for c in c_list:
    dist[c] = dijkstra(graph, c, n)

for v in range(1, n + 1):
    summ = 0
    for c in c_list:
        summ += dist[c][v]

    if summ < answer[1] or (summ == answer[1] and v < answer[0]):
        answer[0] = v
        answer[1] = summ

print(answer[0], answer[1])
"""

#TODO B
#С конца смотреть, куда можно будет дойти за время t, -- их и берем. Транспонировать граф, запустить алгоритм Дейкстры и остановить его, когда достигентся время t

"""
def read_graph_as_edges_list(N): # список ребер, n ребер в графе, индексация вершин с 1
    edges = []
    for i in range(N):
        e = list(map(int,input().split()))
        edges.append(e)
    return edges

def read_graph_as_list(N, M): # список смежности, N вершин, M ребер, индексация вершин с 1
    edges = read_graph_as_edges_list(M)
    adj_dict = {(i + 1): [] for i in range(N)}
    for e in edges:
        adj_dict[e[1]].append((e[0], e[2]))
    return adj_dict

import heapq

def dijkstra(G, s, t): # реализация на кучах
    # G - граф, представленный списком смежности, индексация с 1
    dist = {s: 0}
    prev = [None for i in range(len(G.keys()) + 1)]
    pq = [(0, s)] # (distance, node)
    visited = set()

    while pq:
        cur_dist, v = heapq.heappop(pq)

        if v in visited:
            continue
        visited.add(v)

        for to, weight in G.get(v, []):

            new_dist = cur_dist + weight
            if new_dist > t:
                continue
            if to not in dist or new_dist < dist[to]:
                dist[to] = new_dist
                prev[to] = v
                heapq.heappush(pq, (new_dist, to))

    return dist # parent - словарь вершин, по которым можно восстановить кратчайший путь
    # (для i-ой вершины указана вершина, из которой можно прийти в i-ую вершину за наименьшую цену)

n = int(input())
e = int(input())
t = int(input())
m = int(input())

graph = read_graph_as_list(n, m)

dist = dijkstra(graph, e, t)

print(len(dist))
"""

#TODO C
#Хранить на ребрах время отбытия и время прибытия. В вершинах храним минимальное время прибытия. А также мы не сможем пройти по ребрам, если поезд уже ушел



#TODO D
#Хакеры - листья. Убрать вершины хакеров и построить минимальное остовное дерево, а затем подвесить хакеров так, чтобы к ним вели ребра с минимальной стоимостью, но не через хакеров!
#Для любого хакера должен быть хороший сосед, иначе пример: (X)--(X)--ОК-ОК
#После удаления хакеров должен остаться связанный граф, т.е. мин. остов. дерево должно содержать все вершины



#TODO E
#Двудольный граф: левая доля -- вершины-столбцы, правая доля -- вершины-строки, ребра - свободные клетки. Поиск максимального паросочетания (т.к. тогда мы не сможем провести ребро, инцедентное какому-то занятому столбцу/строке)

"""
def read_graph(cuts, cells, L, R):
    adj_dict = {}
    for i in L:
        adj_dict[i] = [_ for _ in R]
    for i in range(cuts):
        adj_dict[cells[2 * i]].remove(cells[2 * i + 1])

    return adj_dict

def kuhn(graph, L, n):
    match = [-1] * n
    visited = [False] * n
    def dfs(v):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == -1 or dfs(match[u]):
                    match[u] = v
                    return True
        return False

    max_matching = 0
    for v in L:
        visited = [False] * n
        if dfs(v):
            max_matching += 1
    return max_matching

amount = int(input())
answer = []

for i in range(amount):
    rows, cols, cuts = map(int, input().split())
    cells = list(map(int, input().split()))

    L = [_ for _ in range(rows)]
    R = [_ for _ in range(cols)]
    graph = read_graph(cuts, cells, L, R)

    answer.append(kuhn(graph, L, rows + cols))

print(*answer, sep="\n")
"""

#TODO F
#Построить многослойный граф (четырехдольный, а не двудольный с добавлением вспомогательных вершин, каждая связана со своим человеком). Каждый раз, когда вы выбираете студента, то надо ее перераспределять в пару
#
#    1  2  3  4  5
#   _--0--0  0--0--_
# 0 ---0--0  0--0--- 0
#   -__0__0  0__0__-
#
# В слое 3 ставим ребра между теми, кто не хочет друг с другом работать, перебираем capacity в 1 слое, пока не увеличиться поток

#TODO G
#Поиск глобального минимального разреза в графе (т.е. надо перебрать разные комбинации стока и истока)
