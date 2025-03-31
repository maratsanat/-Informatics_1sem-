from collections import deque
def edmonds_karp(graph, source, sink):
    n = len(graph)
    res = [[0] * n for _ in range(n)]
    for u in range(n):
        for v, capacity in graph[u]:
            res[u][v] = capacity   
    m = 0
    parent = [-1] * n   
    def bfs():
        visited = [False] * n
        queue = deque()
        queue.append(source)
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v in range(n):
                if not visited[v] and res[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
                    queue.append(v)
        return False  
    while bfs():
        path = float('inf')
        v = sink
        while v != source:
            u = parent[v]
            path = min(path, res[u][v])
            v = u
        v = sink
        while v != source:
            u = parent[v]
            res[u][v] -= path
            res[v][u] += path
            v = u
        
        m += path
    
    return m