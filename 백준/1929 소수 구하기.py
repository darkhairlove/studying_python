
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
m += 1
arr = [True] * m

for i in range(2, int(m**0.5)+1):
    if arr[i]:
        for j in range(2*i, m, i):
            arr[j] = False
for i in range(n, m):
    if arr[i] != 0 and i > 1:
        print(i)
