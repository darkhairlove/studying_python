import sys
input = sys.stdin.readline
n = int(input())
a = list()
for i in range(n):
    a.append(int(input()))
a.sort()
con = 0
for i in range(1, n+1):
    con += abs(i-a[i-1])
print(con)
