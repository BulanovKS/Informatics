#TODO АЛГОРИТМ ДИНИЦА -- поиск макс. потока

def dinic(G, s, t):
    # BFS для слоистой сети
    def bfs(residual_graph, level):
        queue = [s]
        level[s] = 0

        while queue:
            u = queue.pop(0)
            for v, capacity in residual_graph[u].items():
                if level[v] == -1 and capacity > 0:
                    level[v] = level[u] + 1
                    queue.append(v)

        return level[t] != -1  # Возвращаем True, если сток достижим

    #DFS для блокирующего потока
    def dfs(residual_graph, u, flow, level, ptr):
        if u == t:
            return flow

        while ptr[u] < len(residual_graph[u]):
            v, capacity = list(residual_graph[u].items())[ptr[u]]
            if level[v] == level[u] + 1 and capacity > 0:
                min_capacity = min(flow, capacity)
                pushed = dfs(residual_graph, v, min_capacity, level, ptr)
                if pushed > 0:
                    residual_graph[u][v] -= pushed
                    residual_graph[v][u] = residual_graph[v].get(u, 0) + pushed
                    return pushed
            ptr[u] += 1
        return 0

    # Остаточный граф
    residual_graph = {u: {v: capacity for v, capacity in neighbors.items()} for u, neighbors in G.items()}
    max_flow = 0
    level = {node: -1 for node in G}  # Уровни вершин в слоистой сети

    # Пока сущестсвует слоистая сеть над остаточной
    while bfs(residual_graph, level):
        ptr = {node: 0 for node in G}
        flow = dfs(residual_graph, s, float('Inf'), level, ptr)
        while flow > 0:
            max_flow += flow
            flow = dfs(residual_graph, s, float('Inf'), level, ptr)
        level = {node: -1 for node in G}  # Сбрасываем слоистую сеть следующей итерации

    return max_flow