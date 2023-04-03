arr = list(map(int, input().split()))
arr = sorted(arr)
a1 = arr[0]+arr[1]
if arr[2] >= a1:
    print(a1+a1-1)
else:
    print(sum(arr))
