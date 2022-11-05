#arr = [20, 7, 23, 19, 10, 15, 25, 8, 13]
arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort(reverse=False)
ans = sum(arr) - 100
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == ans:
            for k in range(len(arr)):
                if k == j or k == i:
                    pass
                else:
                    print(arr[k])
            exit()
