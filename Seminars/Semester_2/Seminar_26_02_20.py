from Seminar_26_02_06 import _read_graph_as_matrix

#TODO: ТОПОЛОГИЧЕСКАЯ СОРТИРОВКА (ТАРЬЯНА), КОСАРАЙЮ, ДЕЙКСТРЫ, БОРУВКА

def TopSort(G): # G - граф, представленный списком смежности, индексация с 1
    color = [''] + ['white' for _ in G.keys()]
    topsorted = list()

    def dfs_visit(graph, v):
        color[v] = 'gray'

        for u in graph[v]:
            if color[u] == 'gray':
                print('has cycle')
            if color[u] == 'white':
                dfs_visit(graph, u)

        color[v] = 'black'
        topsorted.append(v)

    for i in range(len(color)):
        if color[i] == 'white':
            dfs_visit(G, i)

    return topsorted[::-1]

#graph = read_graph_as_list(5, 5)
#print(TopSort(graph))

#TODO: КОНДЕНСАЦИЯ ГРАФА, КОСАРАЙЮ

def Kosaraju(G): # определяет компоненты сильной связанности в ориентированном графе
    # G - граф, представленный списком смежности, индексация с 1
    def transpose(G):
        adj_dict = {}
        for v in G.keys():
            adj_dict[v] = []
        for v in G.keys():
            for u in G[v]:
                adj_dict[u].append(v)
        return adj_dict

    def dfs(graph, v, visited, stack):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited, stack)
        stack.append(v)

    stack = []
    visited = [True] + [False] * len(G.keys())
    for i in range(len(G.keys())): # по сути это TopSort, но без проверки на ацикличность
        if not visited[i]:
            dfs(G, i, visited, stack)
    transposed = transpose(G)
    visited = [True] + [False] * len(G.keys())
    scc = []

    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs(transposed, v, visited, component)
            scc.append(component)

    return scc

#graph = read_graph_as_list(7, 9)
#print(Kosaraju(graph))

#TODO: DSU (СИСТЕМА НЕПЕРЕСЕКАЮЩИХСЯ МНОЖЕСТВ), БОРУВКА

class DSU:
    def __init__(self, size):
        self.parent = list(range(size + 1))
        self.rank = [1] * (size + 1)

    def find(self, x): # нахождение корня
        #эвристика сжатия путей
        if self.parent[x] != x: # если parent это не корень
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y): # объединение через нахождение корня
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY: # если они в разных множествах
            if self.rank[rootX] > self.rank[rootY]: #ранговая эвристика
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y): # проверка связанности
        return self.find(x) == self.find(y)

def connected_components(graph): # определяет компоненты связанности в графе, graph - список смежности
    visited = set()
    components = []

    vertices = list(range(len(graph)))

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

def Boruvka(vertices, edges): # определяет минимальное остовное дерево (MST) в неориентированном графе, нумерация с 1
    # vertices - кол-во вершин, edges - список ребер с весами
    dsu = DSU(vertices)
    num_components = vertices
    mst_weight = 0
    mst_edges = []

    while num_components > 1:
        cheapest = [0] + [-1] * vertices
        for i, (u, v, weight) in enumerate(edges): # i - порядковый номер ребра в списке ребер
            set_u = dsu.find(u)
            set_v = dsu.find(v)

            if set_u != set_v:
                if cheapest[set_u] == -1 or edges[cheapest[set_u]][2] > weight:
                    cheapest[set_u] = i
                if cheapest[set_v] == -1 or edges[cheapest[set_v]][2] > weight:
                    cheapest[set_v] = i

        # Объединение компонентов, используя найденные минимальные ребра
        for i in range(vertices):
            if cheapest[i] != -1:
                u, v, weight = edges[cheapest[i]]
                set_u = dsu.find(u)
                set_v = dsu.find(v)

                if set_u != set_v:  # Если ребро соединяет разные компоненты
                    dsu.union(set_u, set_v)
                    mst_edges.append((u, v, weight))
                    mst_weight += weight
                    num_components -= 1

    return mst_edges, mst_weight

#graph = read_graph_as_edges_list(7)
#print(Boruvka(5 ,graph))

#TODO: ДЕЙКСТРЫ, ASTAR (A*), ФОРДА-БЕЛЛМАНА, ФЛОЙДА-УОРШЕЛЛА

def Dijkstra(G,s): # определяет кратчайший путь от вершины s до всех остальных вершин в графе G (веса >= 0)
    # G - граф, представленный списком смежности, индексация с 1
    V = len(G.keys()) + 1
    dist = [float('inf') for i in range(V)]
    prev = [None for i in range(V)]
    dist[s] = 0
    S = set()
    S.add(0)
    while len(S) < V:
        v = dist.index(min(dist)) # можно поменять на кучу
        S.add(v)
        for u, w in G[v]:
            if u not in S and dist[u] > dist[v] + w:
                prev[u] = v
                dist[u] = dist[v] + w
        dist[v] = float('inf')
        print(dist)

    return prev # список вершин, по которым можно восстановить кратчайший путь
    # (для i-ой вершины указана вершина, из которой можно прийти в i-ую вершину за наименьшую цену)

#graph = read_graph_as_list(5,7, True, True)
#print(Dijkstra(graph, 1))

import heapq

def dijkstra(graph, start, goal=None): # реализация на кучах
    dist = {start: 0}
    parent = {start: None}
    pq = [(0, start)] # (distance, node)
    visited = set()

    while pq:
        cur_dist, v = heapq.heappop(pq)

        if v in visited:
            continue
        visited.add(v)

        if goal is not None and v == goal:
            break

        for to, weight in graph.get(v, []):

            new_dist = cur_dist + weight
            if to not in dist or new_dist < dist[to]:
                dist[to] = new_dist
                parent[to] = v
                heapq.heappush(pq, (new_dist, to))

    return dist, parent


def astar(graph, start, goal, heuristic):
    g_score = {start: 0}
    parent = {start: None}

    # (f_score, g_score, node)
    pq = [(heuristic(start, goal), 0, start)]
    closed = set()

    while pq:
        f_cur, g_cur, v = heapq.heappop(pq)

        if v in closed:
            continue
        closed.add(v)

        if v == goal:
            return g_score[v], parent

        for to, weight in graph.get(v, []):

            probe_g = g_score[v] + weight

            if to not in g_score or probe_g < g_score[to]:
                g_score[to] = probe_g
                parent[to] = v
                f_score = probe_g + heuristic(to, goal)
                heapq.heappush(pq, (f_score, probe_g, to))

    return None, parent


def build_grid_graph(n, m, blocked=None):
    if blocked is None:
        blocked = set()

    graph = {}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for x in range(n):
        for y in range(m):
            if (x, y) in blocked:
                continue

            neighbors = []
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in blocked:
                    neighbors.append(((nx, ny), 1))
            graph[(x, y)] = neighbors

    return graph

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def eucledian(a, b):
    return (abs(a[0] - b[0])**2 + abs(a[1] - b[1])**2)**0.5

"""
import time
graph = build_grid_graph(1000, 1000)

start = (0, 0)
goal = (400, 500)

# Dijkstra
t = time.time()
dist, parent_d = dijkstra(graph, start)

print(time.time() - t)
print("Dijkstra distance:", dist.get(goal))


# A*
t = time.time()
astar_dist, parent_a = astar(graph, start, goal, manhattan)
print(time.time() - t)

print("A* distance:", astar_dist)
"""

def BelmanFord(G, s): # решается проблема отриц. ребер и циклов, G - список смежности, нумерация с 1
    V = len(G.keys()) + 1
    dist = [float('inf') for i in range(V)]
    prev = [None for i in range(V)]
    dist[s] = 0
    x = 0

    def relax(v, u, weight, dist, prev):
        if dist[u] > dist[v] + weight:
            dist[u] = dist[v] + weight
            prev[u] = v
            return True
        return False

    for i in range(1,V):
        for v in range(1, V):
            for (u, weight) in G[v]:
                relax(v, u, weight, dist, prev)

    for (u, weight) in G[v]:
        if relax(u, v, weight, dist, prev): return False

    return prev

#graph = read_graph_as_list(5,7, True, True)
#print(BelmanFord(graph, 1))

def FloydWarshall(graph): # решается проблема отриц. ребер и циклов, graph - матрица смежности, индексация с 1
    # ПРИ ИСПОЛЬЗОВАНИИ ЗАМЕНИТЬ НУЛИ В МАТРИЦЕ НА INF (очень большими числами)
    V = len(graph)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    for _ in range(V):
        if graph[_][_] < 0: return False
    return graph

graph = _read_graph_as_matrix(4)
print(FloydWarshall(graph))

"""
100 1 1 100
100 100 1 1
100 100 100 1
100 100 100 100
"""
"""
1 2 1
2 3 5
3 4 2
1 3 7
2 4 3
3 5 10
4 5 1
"""
"""
1 2 1
2 3 1
1 3 1
"""