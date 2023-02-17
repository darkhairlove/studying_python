import sys

input = sys.stdin.readline
t = int(input())

for i in range(t):
    num = int(input())
    arr = []
    for j in range(num):
        x, y = map(int, input().split())
        arr.append([x, y])
    arr.sort()

    a = arr[0][1]
    index = 1
    for j in range(1, num):
        if arr[j][1] < a:
            a = arr[j][1]
            index += 1
    print(index)
