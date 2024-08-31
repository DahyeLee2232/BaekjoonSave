import sys
input = sys.stdin.readline
n = int(input())    #p의 길이는 2n+1
m = int(input())
s = input()

answer = 0
i = 0
cnt = 0
while i < (m - 1):
    if s[i:i+3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(answer)
        