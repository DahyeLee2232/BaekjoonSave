t=int(input())
for i in range(t):
    x=int(input())
    expr = input()
    l = []
    tmp = ''
    for j in range(len(expr)):
        if expr[j] == '+' or expr[j] == '-':
            if len(tmp) != 0:
                l.append(tmp)
            tmp = expr[j]
        else:
            tmp += expr[j]
    l.append(tmp)
    if l[0][0] != '-':
        l[0] = '+' + l[0]

    answer = 0
    for j in l:
        if j.find('X^') != -1:
            idx = j.find('X^')
            if idx == 1:
                if j[0] == '+' :
                    tmp = x ** int(j[idx+2:])
                else:
                    tmp = -(x ** int(j[idx+2:]))
            else:
                tmp = int(j[:idx]) * (x ** int(j[idx+2:]))
        elif j.find('X') != -1:
            idx = j.find('X')
            if idx == 1:
                if j[0] == '+':
                    tmp = x
                else:
                    tmp = -x                 
            else:
                tmp = int(j[:idx]) * x
        else:
            tmp = int(j)
        answer += tmp
    print(f'Case #{i+1}: {answer}')