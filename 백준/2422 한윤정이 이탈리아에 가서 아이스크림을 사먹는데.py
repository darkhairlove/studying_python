import sys

n, m = map(int, input().split())
answer = n * (n - 1) * (n - 2) // 6
nomat = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    answer -= (n-2) - len(nomat[a-1] | nomat[b-1])
    nomat[a-1].add(b)
    nomat[b-1].add(a)

print(answer)
