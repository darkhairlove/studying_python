num = int(input())

for i in range(num):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    nu = int(input())
    for i in range(nu):
        c_x, c_y, r = map(int, input().split())
        d1 = (((x1 - c_x) ** 2) + ((y1 - c_y) ** 2)) ** 0.5
        d2 = (((x2 - c_x) ** 2) + ((y2 - c_y) ** 2)) ** 0.5
        if (d1 < r and d2 > r) or (d1 > r and d2 < r):
            cnt += 1
    print(cnt)
    