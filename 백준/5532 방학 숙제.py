

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A % C == 0:
    d = A // C
else:
    d = (A // C) + 1

if B % D == 0:
    e = B // D
else:
    e = (B // D) + 1

print(L-max(d, e))
