import heapq
M, N = map(int, input().strip().split())
G = {}
for _ in range(M):
    v1, v2, w = map(int, input().strip().split())
    if v1 not in G:
        G[v1] = {}
    if v2 not in G:
        G[v2] = {}       
    G[v1][v2] = w  
def bellman_ford(G, start):
    d = {i: float('inf') for i in range(N)}
    d[start] = 0
    for _ in range(N - 1):
        for node1 in G:
            for node2 in G[node1]:
                if d[node2] > d[node1] + G[node1][node2]:
                    d[node2] = d[node1] + G[node1][node2]
    return d
def dijkstra(G, start):
    distances = {i: float('infinity') for i in range(N)}
    distances[start] = 0
    h = [(0, start)]
    while h:
        cur_dist, cur_node = heapq.heappop(h)
        if cur_dist > distances[cur_node]:
            continue
        for neighbor in G[cur_node]:
            distance = cur_dist + G[cur_node][neighbor]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(h, (distance, neighbor))
    return distances
def johnson(G):
    new_vertex = N
    G[new_vertex] = {}
    for node in range(N):
        G[new_vertex][node] = 0  
    f = bellman_ford(G, new_vertex)
    new_G = {node: {} for node in range(N)}
    for u in G:
        for v in G[u]:
            if u != new_vertex and v != new_vertex:
                new_weight = G[u][v] + f[u] - f[v]
                new_G.setdefault(u, {})[v] = new_weight
    distances = {}
    for node in range(N):
        distances[node] = dijkstra(new_G, node)
    for u in distances:
        for v in distances[u]:
            distances[u][v] += f[v] - f[u]

    return distances
result = johnson(G)
for i in range(N):
    line = []
    for j in range(N):
        if result[i][j] == float('inf'):
            line.append('inf')
        else:
            line.append(str(result[i][j]))
    print(' '.join(line))
