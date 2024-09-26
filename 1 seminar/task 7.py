a = list(input().split())
w = 1
for i in range(len(a)):
    if a.count(a[i]) >= w:
        w = a.count(a[i])
        ans = a[i]
print(ans)