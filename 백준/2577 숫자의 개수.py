
arr = []

k = 1
for i in range(3):
    arr.append(int(input()))

    k = k * arr[i]
j = list(str(k))

for i in range(0, 10):
    print(j.count(str(i)))
