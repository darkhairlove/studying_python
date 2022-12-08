num = int(input())

arr = list(map(int, input().split()))
arr = list(sorted(set(arr)))
for i in arr:
    print(i, end=' ')
