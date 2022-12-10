import sys
input = sys.stdin.readline
A = int(input())

cut = 0
arr2 = list()
arr = map(int, input().split())
a, b = map(int, input().split())
for i in arr:
    i -= a
    cut += 1
    if i > 0:
        if i % b:
            cut += i//b + 1
        else:
            cut += i//b
print(cut)
