num = int(input())

for i in range(num):
    a, b, r_1, c, d, r_2 = list(map(int, input().split()))
    d = ((a-c)**2 + (b-d)**2)**(1/2)
    r = r_2+r_1
    if r_1 <= r_2:
        r1 = r_2 - r_1
    else:
        r1 = r_1 - r_2
    if r1 < d < r:
        print("2")
    elif d > r or d < r1:
        print("0")
    elif d == 0 and r1 == 0:
        print("-1")
    elif d == r or d == r1:
        print("1")
