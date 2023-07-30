num = int(input())
arr = []
for i in range(num):
    arr.append(input())
con = 0
arr.sort()
ar2 = arr
for i in range(num):
    an = False
    for j in range(i+1, num):
        if arr[i] == arr[j][0:len(arr[i])]:
            an = True
            break
    if not an:
        con += 1
print(con)
