for _ in range(int(input())):
    n = int(input())
    stick = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]
    for i in range(2):
        dp[i][0] = stick[i][0]
        if n > 1:
            dp[i][1] = stick[1-i][0]+stick[i][1]
    for j in range(2, n):
        for i in range(2):
            dp[i][j] = max(dp[1-i][j-2], dp[1-i][j-1])+stick[i][j]

    print(max(dp[0][n-1], dp[1][n-1]))
