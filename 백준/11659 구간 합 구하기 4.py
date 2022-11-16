import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = list(map(int, input().split()))
arrsum = 0
arrs = [0]

for i in range(N):
    arrsum += arr[i]
    arrs.append(arrsum)
for _ in range(M):
    a, b = map(int, input().split())
    print(arrs[b]-arrs[a-1])
