from sys import stdin
num = int(input())
arr = []

s = stdin.readline().rstrip()

for i in range(0, len(s), num):
    arr.append(list(s[i:i+num]))


for i in range(len(arr)):
    if i % 2 != 0:
        data = list(reversed(arr[i]))
        arr[i] = data
res = ''
for j in range(num):
    for i in range(len(arr)):
        res += arr[i][j]
print(res)
