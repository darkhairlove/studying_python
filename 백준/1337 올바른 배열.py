n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr = sorted(arr)

re_arr = []

for i in range(0, n):
    con = 0
    for j in range(arr[i], arr[i]+5):
        if j not in arr:
            con += 1
    re_arr.append(con)
print(min(re_arr))
