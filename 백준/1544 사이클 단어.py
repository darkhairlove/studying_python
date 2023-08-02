num = int(input())
arr = []
for i in range(num):
    arr.append(input())
for i in arr:
    se = []
    for k in range(len(i)-1):
        se.append(i[k+1:]+i[0:k+1])

    for m in se:
        if m in arr and i != m:
            arr.remove(m)

print(len(set(arr)))
