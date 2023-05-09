num = int(input())
arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]

for i in range(1, num):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += arr[i]
print(max(dp))
