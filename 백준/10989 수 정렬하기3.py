import sys

num = int(sys.stdin.readline())
arr = [0] * 10001

for i in range(num):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
