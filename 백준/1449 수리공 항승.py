arr = [False]*1001
N, L = map(int, input().split())

for i in map(int, input().split()):
    arr[i] = True

ans = 0
x = 0
while x <= 1000:
    if arr[x]:
        ans += 1
        x += L
    else:
        x += 1

print(ans)
