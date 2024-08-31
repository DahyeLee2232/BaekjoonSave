N = int(input())
weight_list = sorted(list(map(int, input().split())))
m_sum = 1

for i in range(N):
    if m_sum < weight_list[i]:
        break
    m_sum += weight_list[i]
print(m_sum)