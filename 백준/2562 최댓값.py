
arr = []
for i in range(9):
    arr.append(int(input()))

print(max(arr))
D = int(arr.index(max(arr))+1)
print(D)
