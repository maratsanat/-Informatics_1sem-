def convert(zf):
    if not zf:
        return ''  
    n = len(zf)
    word = [''] * n
    word[0] = 'A' 
    curr_char = ord('B') 
    
    left, right = 0, 0 
    
    for i in range(1, n):
        if i > right:
            if zf[i] == 0:
                word[i] = chr(curr_char)
                curr_char += 1
                left, right = i, i  
            else:
                for j in range(zf[i]):
                    if i + j >= n:
                        break
                    word[i + j] = word[j]
                right = i + zf[i] - 1
                left = i
        else:
            pos = i - left
            if zf[pos] < right - i + 1:
                word[i] = word[pos]
            else:
                for j in range(right - i + 1, zf[pos]):
                    if i + j >= n:
                        break
                    word[i + j] = word[j]
                left = i
                right = i + zf[pos] - 1
    
    return ''.join(word)

zf1 = [0,0,0,0]
print(convert(zf1)) 
