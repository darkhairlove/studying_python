import sys
input = sys.stdin.readline
num = int(input())
arr = []
for i in range(num):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)
for i in arr:
    print(i)
