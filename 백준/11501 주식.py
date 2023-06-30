num = int(input())
for _ in range(num):
    s = int(input())
    arr = list(map(int, input().split()))
    m = 0
    val = 0
    for i in range(len(arr)-1, -1, -1):
        if arr[i] > m:
            m = arr[i]
        else:
            val += m-arr[i]
    print(val)
