a, b = map(int, input().split())
arr = []
for i in range(a):
    arr.append(input())
check = min(a, b)
ans = 0
for i in range(a):
    for j in range(b):
        for k in range(check):
            if (i+k < a) and j+k < b and arr[i][j] == arr[i][j+k] == arr[i+k][j] == arr[i+k][j+k]:
                ans = max(ans, (k+1)**2)
print(ans)
