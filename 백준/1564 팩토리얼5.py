import math
import sys
arr = []
input = sys.stdin.readline
n = int(input())
fact = str(math.factorial(n))
cnt = 0
for i in fact[::-1]:
    if i == '0':
        continue
    if cnt == 5:
        break
    else:
        arr.append(i)
        cnt += 1
for a in arr:
    print(a, end='')
