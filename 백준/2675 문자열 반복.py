
num = int(input())
arr = []
for i in range(num):
    arr = list(input())
    val = int(arr[0])

res = []
i = 2
for i in range(2, len(arr)):
    for j in arr[i]:
        res.append(val*j)
print(''.join(res))
