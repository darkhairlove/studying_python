import sys
input = sys.stdin.readline
num = int(input())

for _ in range(num):
    a, b = map(int, input().split())
    a %= 10
    if a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        b %= 4
        if b == 0:
            print((a**4) % 10)
        else:
            print((a**b) % 10)
    elif a == 0:
        print(10)
    else:
        b %= 2
        if b == 0:
            print((a**2) % 10)
        else:
            print((a**(b % 2)) % 10)
