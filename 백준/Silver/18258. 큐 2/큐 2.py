import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque([])
for i in range(n):
    oper = input().split()
    if oper[0] == 'push':
        queue.append(oper[1])
    elif oper[0] == 'pop':
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif oper[0] == 'size':
        print(len(queue))
    elif oper[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif oper[0] == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif oper[0] == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
