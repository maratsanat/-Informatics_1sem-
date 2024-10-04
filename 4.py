def triangle(size,symb,cur=1):
    if size==0:
        return
    print(min(cur,size)*symb)
    triangle(size-1,symb,cur+1)
