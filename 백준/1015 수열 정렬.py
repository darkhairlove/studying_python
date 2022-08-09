import sys
input = sys.stdin.readline

num = int(input())
arr = list(map(int, input().split()))
arr2 = list()
for i in range(num):
    arr2.append([i, arr[i]])
arr2 = sorted(arr2, key=lambda x: x[1])
for i in range(num):
    arr2[i][1] = i
arr2 = sorted(arr2, key=lambda x: x[0])
for i in range(num):
    print(arr2[i][1], end=" ")
