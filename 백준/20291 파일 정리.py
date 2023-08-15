num = int(input())
arr = {}
for i in range(num):
    a, c = input().split('.')

    if c not in arr:
        arr[c] = 1
    else:
        arr[c] += 1
arr = sorted(arr.items())

for i in arr:
    print(i[0], i[1])
