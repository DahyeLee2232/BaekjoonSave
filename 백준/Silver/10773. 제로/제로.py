stack = []
k = int(input())
for i in range(k):
    n = int(input())
    if n == 0:
        del stack[-1]
    else:
        stack.append(n)
print(sum(stack))