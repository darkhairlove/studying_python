import math
import sys
input = sys.stdin.readline
n = int(input())
fact = str(math.factorial(n))
for i in fact[::-1]:
    if i == '0':
        continue
    else:
        print(i)
        break
