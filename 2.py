def factor(n, i=2):
    while (i*i<= n):
        if n%i !=0:
            i+=1
        else:
            return[i]+factor(n//i,i)
    return[n]
print(factor(1000))
