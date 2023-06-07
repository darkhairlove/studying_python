num = int(input())
arr = []
a = int(input())
for _ in range(num-1):
    arr.append(int(input()))
arr.sort(reverse=True)
ans = 0
while True:
    if len(arr) == 0:
        print(0)
        break
    if a <= arr[0]:
        arr[0] -= 1
        a += 1
        ans += 1
        arr.sort(reverse=True)
    else:
        print(ans)
        break
