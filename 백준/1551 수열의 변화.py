n, m = map(int, input().split())
arr = list(map(int, input().split(',')))
for _ in range(m):
    temp = []
    for i in range(1, len(arr)):
        temp.append(arr[i]-arr[i-1])
    arr = temp
    temp = []
print(','.join(map(str, arr)))
