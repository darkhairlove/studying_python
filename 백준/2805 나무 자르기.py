n, m = map(int, input().split())
arr = list(map(int, input().split()))
l0 = 0
high = max(arr)
mid = (l0 + high)//2
def get(h):
    ret = 0
    for i in arr:
        if i > h:
            ret += i-h
    return ret
ans =0
while l0<=high:
    if get(mid) >= m:
        ans = mid
        l0 = mid+1
    else:
        high = mid -1
    mid= (l0+high)//2
print(ans)
    