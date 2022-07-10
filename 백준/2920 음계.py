arr = list(map(int, input().split()))
arr2 = 0

if arr[0] == 1:
    for i in range(0, len(arr)-1):
        if arr[i+1] > arr[i]:
            arr2 += 1
elif arr[0] == 8:
    for i in range(0, len(arr)-1):
        if arr[i+1] < arr[i]:
            arr2 += -1
if arr2 == 7:
    print("ascending")
elif arr2 == -7:
    print("descending")
else:
    print("mixed")
