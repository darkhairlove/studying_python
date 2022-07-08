
arr = list(input())

res = []
j = 97
for i in range(26):
    if chr(j) in arr:
        res.append(arr.index(chr(j)))
    else:
        res.append(-1)
    j += 1
print(*res)
