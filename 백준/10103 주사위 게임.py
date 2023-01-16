# https://www.acmicpc.net/problem/10103
num = int(input())
c = 100
s = 100
for i in range(num):
    a, b = map(int, input().split())
    if a > b:
        s -= a
    elif a < b:
        c -= b
print(c)
print(s)
