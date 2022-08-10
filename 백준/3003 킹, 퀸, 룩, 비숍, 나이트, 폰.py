num = list(map(int, input().split()))
arr = [1, 1, 2, 2, 2, 8]
lis = []
j = 0
for i in arr:
    lis.append(i-num[j])
    j += 1
for i in lis:
    print(i, end=" ")
