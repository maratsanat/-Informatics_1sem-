N = int(input())
a = list(input().split())
p = 0
for i in a:
    for j in a:
        if i > j:
            p += 1
    if p == ((N - 1)/2):
            print(i)
            break