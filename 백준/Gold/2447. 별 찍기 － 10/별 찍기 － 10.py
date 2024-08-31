def star(n):
    if n==1:
        return ['*']
    
    s = star(n // 3)
    sl = []
    
    for i in s:
        sl.append(i*3)
    for i in s:
        sl.append(i + ' '*(n//3) + i)
    for i in s:
        sl.append(i*3)
    return sl

n = int(input())
print('\n'.join(star(n)))