f = list(input().split())
res = ''.join(f)
l = res[::-1]
a = res.replace('E', '*').replace('J', '?').replace('S', '!').replace('Z', '-')
a = a.replace('3', '@').replace('L', '#').replace('2', '$').replace('5', '+')
a = a.replace('*', '3').replace('?', 'L').replace('!', '2').replace('-', '5')
a = a.replace('@', 'E').replace('#', 'J').replace('$', 'S').replace('+', 'Z')
zer = a[::-1]
ban = ['B', 'C', 'D', 'F', 'G', 'K', 'N', 'P', 'Q', 'R', '4', '6', '7', '9']
p = 0
for i in range(len(ban)-1):
    if ban[i] in f:
        p +=1
        if res == l:
            print(res, "is a regular palindrome")# E A 3     * A @    3 A E    E A 3
            break
        else:
            print(res, "is not a palindrome")
            break
if p == 0:
    if zer == res:
        if res == l:
            print(res, "is a mirrored palindrome")
        else:
            print(res, "is a mirrored string")