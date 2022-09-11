num = list(map(int, input().split()))
n = min(num)

while 1:
    con = 0
    for i in range(5):
        if n % num[i] == 0:
            con += 1
    if con > 2:
        print(n)
        break
    n += 1
