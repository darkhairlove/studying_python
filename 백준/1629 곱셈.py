
import sys
input = sys.stdin.readline


def pow(a, b, c):
    if b == 1:
        return a % c
    else:
        k = pow(a, b//2, c)
        if b % 2 == 0:
            return k*k % c
        else:
            return k*k*a % c


a, b, c = map(int, input().split())
print(pow(a, b, c))
