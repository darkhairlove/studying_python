arr = input()
a = list()
for i in arr:
    a.append(i)


for i in range(len(a)):
    min_index = i
    for j in range(i+1, len(a)):
        if a[min_index] < a[j]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]
for i in a:
    print(i, end="")
