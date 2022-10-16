import sys
input = sys.stdin.readline

T = int(input())
lis = []
for _ in range(T):
    n = int(input())
    lis.append(n)

dp = [0] * (max(lis)+1)

dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, len(dp)):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for n in lis:
    print(dp[n])
