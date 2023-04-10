N = int(input())
ans = 0
col = [False]*N
d1 = [False]*2*N
d2 = [False]*2*N


def back(row):
    global ans
    if row == N:
        ans += 1
        return
    for j in range(N if row else N//2):
        if not col[j] and not d1[row-j] and not d2[row + j]:
            col[j] = True
            d1[row-j] = True
            d2[row + j] = True

            back(row+1)

            d2[row+j] = False
            d1[row-j] = False
            col[j] = False


if N % 2:
    back(0)
    ans *= 2
    j = N//2
    col[j] = d1[-j] = d2[j] = True
    back(1)
    print(ans)
else:
    back(0)
    print(ans*2)
