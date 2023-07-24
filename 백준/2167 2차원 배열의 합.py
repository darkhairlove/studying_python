# 시간 초과
# N, M = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(N)]
# L = int(input())

# for _ in range(L):
#     ans = 0
#     a, b, n, x = map(int, input().split())
#     for i in range(a-1, n):
#         for k in range(b-1, x):
#             ans += arr[i][k]
#     print(ans)

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
memo = [[0] * (M+1) for _ in range(N+1)]

for m in range(1, N+1):
    for n in range(1, M+1):
        memo[m][n] = memo[m][n-1] + memo[m-1][n]-memo[m-1][n-1] + arr[m-1][n-1]


L = int(input())

for _ in range(L):
    a, b, n, x = map(int, input().split())
    print(memo[n][x]-memo[a-1][x]-memo[n][b-1] + memo[a-1][b-1])
