# TODO: АЛГОРИТМ КУНА

def bipartite(graph):
    n = len(graph.keys())
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            queue = [start]
            colors[start] = 0

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    # Если сосед уже окрашен в тот же цвет, граф не двудольный
                    elif colors[v] == colors[u]:
                        return False, []

    set1 = [i for i in range(n) if colors[i] == 0]
    set2 = [i for i in range(n) if colors[i] == 1]

    return True, (set1, set2)

def kuhn(graph):
    n = len(graph.keys())
    match = [-1] * n
    visited = [False] * n
    _, parts = bipartite(graph)
    L = parts[0]
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
