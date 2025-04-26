def count(p, text):
    n = len(p)
    if n == 0 or len(text) == 0:
        return 0
    s = [p[i:] + p[:i] for i in range(n)]
    unique_s = set(s)
    count = 0
    s_len = n
    text_len = len(text)
    for shift in unique_s:
        for i in range(text_len - s_len + 1):
            if text[i:i+s_len] == shift:
                count += 1
                
    return count
