# https://www.acmicpc.net/problem/1764
n, m = map(int, input().split())
arr1 = []
arr2 = []
for i in range(n):
    arr1.append(input())

for i in range(m):
    arr2.append(input())

s1 = set(arr1)
s2 = set(arr2)

a = list(s1 & s2)

print(len(a))
a.sort()
for i in a:
    print(i)
