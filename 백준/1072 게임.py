# -- 시간 초과 --
a, b = map(int, input().split())
z_old = (b * 100 / a)
cut = 0
while 1:
    if z_old >= 99:
        cut = -1
        break
    b += 1
    a += 1
    cut += 1
    z_new = (b * 100 / a)
    if z_new > z_old:
        break

print(cut)

# -- 이분 탐색으로 풀기 --
a, b = map(int, input().split())
z_old = (b * 100 // a)

if z_old >= 99:
    print(-1)
else:
    end = 1000000000
    start = 1
    ans = 0
    while start <= end:
        mid = (start+end)//2
        if (b + mid) * 100 // (a + mid) > z_old:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1
    print(ans)
