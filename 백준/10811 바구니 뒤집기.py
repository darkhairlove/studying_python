import sys

n, m = map(int, sys.stdin.readline().split())
tmp = []
for i in range(n):
    tmp.append(i+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    tmp[a-1:b] = tmp[a-1:b][::-1]
print(*tmp)
