a, b = map(int, input().split())
arr1 = list()
for i in range(a):
    arr1.append(list(map(int, input().split())))

c, d = map(int, input().split())
arr2 = list()
for i in range(c):
    arr2.append(list(map(int, input().split())))

an = [len(arr2[0])*[0] for i in range(len(arr1))]
for i in range(len(an)):
    for j in range(len(an[i])):
        for k in range(len(arr1[i])):
            an[i][j] += arr1[i][k] * arr2[k][j]
for i in range(len(an)):
    for k in range(len(an[0])):
        print(an[i][k], end=' ')
    print()
