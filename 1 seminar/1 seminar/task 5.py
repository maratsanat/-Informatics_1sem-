n, b, c = int(input()), int(input()), int(input())
dn = 0
vol = 0
res = ''

for i in str(n)[::-1]:                  
    dn += int(i) * (b ** vol)
    vol += 1

while dn > 0:
    last_d = dn % c                     
    res = str(last_d) + res             
    dn //= c

print(res)                              
     