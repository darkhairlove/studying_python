
num = int(input())
arr = list()

for i in range(num):
    arr.append(list(input()))

for i in range(num):
    res = []
    val = int(arr[i][0])
    for j in range(2, len(arr[i])):
        res.append(val*arr[i][j])
    print(''.join(res))
