

A = int(input())
arr = []

for i in range(A):
    arr.append(input())
    arr[i] = arr[i].split('X')
    i += 1
    print(arr, i)

count = 0
j = 0
for j in arr:
    if 'O' in j:
        count += 1
print(count, j)

# for i in range(0, 10):
#   print(j.count(str(i)))
