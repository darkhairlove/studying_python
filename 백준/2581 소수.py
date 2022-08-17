import sys
input = sys.stdin.readline


def is_prime_number(x):
    if x == 1:
        return False
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True


M = int(input())
N = int(input())
sum = 0
li = []
for x in range(M, N+1):
    if is_prime_number(x):
        sum += x
        li.append(x)
if sum > 0:
    print(sum)
    print(min(li))
else:
    print(-1)
