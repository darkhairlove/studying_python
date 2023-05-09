num = int(input())

dp = [i for i in range(num+1)]

for i in range(4, num+1):
    for j in range(1, i):
        if i < j*j:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1
print(dp[num])
