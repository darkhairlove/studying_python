
a, b = map(int, input().split())
arr = [True for i in range(a+1)]
con = 0
for i in range(2, len(arr)+1):
    for j in range(i, a+1, i):
        if arr[j] == True:
            arr[j] = False
            con += 1
            if b == con:
                print(j)
                break
