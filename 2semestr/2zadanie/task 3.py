from collections import deque

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if sum(a) != sum(b):
        print("NO")
        return
    size = 2*n + 2
    graph = [[0]*size for _ in range(size)]
    for i in range(1, n+1):
        graph[0][i] = a[i-1]
    for j in range(n+1, 2*n+1):
        graph[j][2*n+1] = b[j-n-1]
    for i in range(1, n+1):
        for j in range(n+1, 2*n+1):
            graph[i][j] = float('inf')
# наверное надо использовать эдмонда-карпа но не догадался как 