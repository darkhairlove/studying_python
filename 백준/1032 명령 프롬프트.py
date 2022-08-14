num = int(input())
arr = list(input())
a_len = len(arr)

for i in range(num-1):
    b = list(input())
    for j in range(a_len):
        if arr[j] != b[j]:
            arr[j] = "?"
print("".join(arr))
