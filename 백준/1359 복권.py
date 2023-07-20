from itertools import combinations
n, m, k = map(int, input().split())

ans = 0
all = [*combinations([i for i in range(n)], m)]

for i in all:
    con = 0
    for j in range(m):
        if i[j] < m:
            con += 1
    if con >= k:
        ans += 1

print(ans/len(all))
