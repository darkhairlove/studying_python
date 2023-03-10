import sys
input = sys.stdin.readline

num = int(input())
arr = [list(input()) for _ in range(num)]
ans = 1


def search():
    global ans
    for i in range(num):
        cnt = 1
        for j in range(1, num):
            if arr[i][j-1] == arr[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
    for j in range(num):
        cnt = 1
        for i in range(1, num):
            if arr[i-1][j] == arr[i][j]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1


for i in range(num):
    for j in range(num):
        if j+1 < num:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            search()
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i+1 < num:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            search()
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(ans)
