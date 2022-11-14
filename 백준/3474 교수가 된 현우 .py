import sys
b = int(input())

for _ in range(b):
    n = int(sys.stdin.readline())
    cont = 0
    i = 5
    while i <= n:
        cont += n // i
        i *= 5
    print(cont)
