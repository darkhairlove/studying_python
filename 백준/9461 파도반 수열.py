arr = [0 for i in range(101)]
arr[1] = 1
arr[2] = 1
arr[3] = 1
for i in range(0, 98):
    arr[i + 3] = arr[i] + arr[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(arr[n])
