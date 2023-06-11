import sys
input = sys.stdin.readline

num = int(input())

for _ in range(num):
    a = int(input())
    arr = set(map(int, input().split()))
    b = int(input())
    arr2 = list(map(int, input().split()))

    for i in arr2:
        if i in arr:
            print(1)
        else:
            print(0)
