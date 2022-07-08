

A = int(input())

arr = list()
for i in range(A):
    arr.append(list(input()))

for i in range(0, A):
    count = 0
    sum = 0
    for j in range(0, len(arr[i])):
        if 'O' in arr[i][j]:
            count += 1
            sum = sum + count
        else:
            count = 0
    print(sum)
