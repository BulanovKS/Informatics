#TODO: ПРЕДСТАВЛЕНИЕ И СЧИТЫВАНИЕ ГРАФОВ

def read_graph_as_edges_list(n): # список ребер, n ребер в графе, индексация вершин с 1
    edges = []
    for i in range(n):
        e = list(map(int,input().split()))
        edges.append(e)
    return edges

def _read_graph_as_matrix(n): # матрица смежности, n ребер в графе, индексация вершин с 1
    M = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        row = list(map(int, input().split()))
        M[i] = row
    return M

def read_graph_as_list(N, M, oriented = True, weighted = False): # список смежности, N вершин, M ребер, индексация вершин с 1
    edges = read_graph_as_edges_list(M)
    adj_dict = {(i + 1): [] for i in range(N)}
    for e in edges:
        if not weighted:
            adj_dict[e[0]].append(e[1])
            if not oriented:
                adj_dict[e[1]].append(e[0])
        if weighted:
            adj_dict[e[0]].append((e[1], e[2]))
            if not oriented:
                adj_dict[e[1]].append((e[0], e[2]))
    return adj_dict

def find_edge(graph, first, second):
    if (first in graph and second in graph[first]) or (second in graph and first in graph[second]):
        return True
    else:
        return False

def read_graph_as_matrix(N, weighted = False): # матрица смежности -> список смежности, N ребер в графе, индексация вершин с 1
    M = _read_graph_as_matrix(N)
    adj_dict = {(i + 1): [] for i in range(N)}
    for i in range(N):
        for j in range(N):
            if M[i][j]:
                if not weighted:
                    adj_dict[i+1].append(j+1)
                else:
                    adj_dict[i+1].append((j+1, M[i][j]))
    return adj_dict

#TODO: ОБХОДЫ ГРАФОВ -- BFS и DFS

def bfs(graph, start): # graph - граф, представленный списком смежности
    visited = set()
    queue = []

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0)
        print(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

#visited = [False for _ in graph.keys()]
def dfs(graph, v, visited, stack):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, stack)
    stack.append(v)

def DFS(graph, v, prev):
    stack = [v]
    while stack:
        node = stack.pop()
        if node not in prev:
            prev.add(node)
        unvisited_neighbors = set(graph[node]) - prev
        stack.extend(unvisited_neighbors)
    return prev