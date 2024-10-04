def fib(n, c = {0:0,1:1}):
    if n in c:
        return c[n]
    c[n]=fib(n-1)+fib(n-2)
    return c[n]
print(fib(500))
