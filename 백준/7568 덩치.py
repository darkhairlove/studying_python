n = int(input())
arr = []
for i in range(n):
    a, b = list(map(int, input().split()))
    arr.append((a, b))
for i in arr:
    sum = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            sum += 1
    print(sum, end=" ")
