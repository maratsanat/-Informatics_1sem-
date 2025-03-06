n, m = map(int, input().split())
adj = {i: set() for i in range(n)}

c = [0] * n
start = 0
for edge in range(m):
    vertex_a, vertex_b = map(int, input().split())
    adj[vertex_a].add(vertex_b)
    adj[vertex_b].add(vertex_a)
    if edge == 0:
        start = vertex_a
    c[vertex_a] += 1
    c[vertex_b] += 1
vertices = []
odd = 0
for idx in range(n):
    if c[idx] % 2 != 0:
        odd += 1
        vertices.append(idx)
visited = []
def dfs(G, visited, start):
    visited.append(start)
    for neighbor in G[start]:
        if neighbor not in visited:
            dfs(G, visited, neighbor)
component = []
dfs(adj, visited, start)
if odd == 2 and len(visited) == n:
    result = []  
    def construct_path(curr):
        while adj[curr]:
            next_vertex = adj[curr].pop()
            adj[next_vertex].remove(curr)
            construct_path(next_vertex)
        result.append(curr)
    construct_path(vertices[0])
    print(*result[::-1])
else:
    print('no way')