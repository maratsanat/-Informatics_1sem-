M, N = map(int, input().split())
G = {}
for _ in range(M):
    v1, v2 = input().split()
    if v1 not in G:
        G[v1] = set()
    if v2 not in G:
        G[v2] = set()
    G[v1].add(v2)
    G[v2].add(v1)
def dfs(G, visited, matching, u):
    for v in G[u]:
        if v not in visited:
            visited.add(v)
            if matching[v] is None or dfs(G, visited, matching, matching[v]):
                matching[v] = u
                return True
    return False
def kuhn(G):
    matching = {v: None for v in G}
    for u in G:
        visited = set()
        dfs(G, visited, matching, u)
    return matching
matching = kuhn(G)
edge_cover = set()
for u, v in matching.items():
    if v is not None and (v, u) not in edge_cover:
        edge_cover.add((u, v))
uncovered = {v for v in G if matching[v] is None}
for u in uncovered:
    for v in G[u]:
        if (u, v) not in edge_cover and (v, u) not in edge_cover:
            edge_cover.add((u, v))
            break 
print()
for edge in edge_cover:
    print(edge[0], edge[1])