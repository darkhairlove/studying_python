
num1, num2 = map(int, input().split())

arr1, arr2 = [], []
for i in [arr1, arr2]:
    for j in range(num1):
        i.append(list(map(int, input().split())))

for i in range(num1):
    for j in range(num2):
        arr1[i][j] += arr2[i][j]
    print(*arr1[i])
