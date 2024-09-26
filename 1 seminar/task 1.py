a = list(map(int, input().split()))
n = a[0]
l=a[1:len(a)]
N = int(n)
S = (N*(1+N))/2
for i in range(len(l)):
    S = S - l[i]
print(S)
print(l)