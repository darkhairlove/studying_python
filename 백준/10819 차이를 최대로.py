import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())

arr = list(map(int, input().split()))

per = permutations(arr, n)

ans = []
for i in per:
    s = 0
    for k in range(1, n):
        s += abs(i[k-1]-i[k])
    ans.append(s)
print(max(ans))
