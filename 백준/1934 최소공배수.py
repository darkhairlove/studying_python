
import sys
input = sys.stdin.readline
num = int(input())

for i in range(num):
    a, b = map(int, input().strip().split())
    A, B = a, b

    while B != 0:
        A = A % B
        A, B = B, A

    print(a*b//A)
