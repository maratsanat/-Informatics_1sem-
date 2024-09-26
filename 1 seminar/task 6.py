a = list(input().split())
c = 0
for i in range(len(a)):
    for k in range(len(a)):
        if a[i]==a[k]:
            c += 1
    if c == 1:
        print(a[i])
        break
  