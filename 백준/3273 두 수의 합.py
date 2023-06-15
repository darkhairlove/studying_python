num = int(input())
arr = sorted(list(map(int, input().split())))
s = int(input())

ans = 0
left, right = 0, num-1
while left < right:
    temp = arr[left] + arr[right]
    if temp == s:
        ans += 1
        left += 1
    elif temp < s:
        left += 1
    else:
        right -= 1
print(ans)
