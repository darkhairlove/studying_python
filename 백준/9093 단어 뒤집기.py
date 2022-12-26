# https://www.acmicpc.net/problem/9093
num = int(input())

for i in range(num):
    arr = list(map(str, input().split()))
    arr2 = list()
    for i in arr:
        arr2.append(i[::-1])
    print(" ".join(arr2))
    continue
