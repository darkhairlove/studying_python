arr = input()
brr = list()
for i in arr:
    brr.append(i)
co = 10
j = 1
for i in range(0, len(brr)):
    if j <= len(brr)-1:
        if brr[i] == brr[j]:
            co += 5
        else:
            co += 10
        j += 1
    else:
        break

print(co)
