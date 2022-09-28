arr = [0 for i in range(1001)]
arr[1] = 1
arr[2] = 2
for i in range(3, 1001, 1):
    arr[i] = arr[i-1] + arr[i-2]
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    con = 0
    for i in range(1, 1001, 1):
        if a <= arr[i] and arr[i] <= b:
            con += 1
    print(con)
