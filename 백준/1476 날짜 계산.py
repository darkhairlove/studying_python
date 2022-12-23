# https://www.acmicpc.net/problem/1476

a, b, c = map(int, input().split())

e = 0
s = 0
m = 0
con = 0

while True:
    e += 1
    s += 1
    m += 1
    con += 1
    if a == e and b == s and c == m:
        print(con)
        break
    if e == 15:
        e = 0
    if s == 28:
        s = 0
    if m == 19:
        m = 0
