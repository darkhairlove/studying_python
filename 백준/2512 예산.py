n1 = int(input())
arr = list(map(int, input().split()))
n2 = int(input())
son = max(arr)
min_ = 1
# 이분 탐색
while son >= min_:
    mid = (son+min_)//2
    res = 0
    for i in arr:
        if mid < i:
            res += mid
        else:
            res += i

    if res > n2:
        son = mid-1
    else:
        min_ = mid+1
print(son)
