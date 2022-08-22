
import sys
input = sys.stdin.readline


while True:
    n = int(input())
    m = 2*n
    arr = [True] * m
    count = 0
    if n == 1:
        print(1)
    elif n != 0:
        for i in range(2, int(m**0.5)+1):
            if arr[i]:
                for j in range(2*i, m, i):
                    arr[j] = False
        for i in range(n+1, m):
            if arr[i] != 0 and i > 1:
                count += 1
        print(count)
    else:
        break
