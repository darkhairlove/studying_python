a = {}
for i in range(8):
    a[i+1] = int(input())
a = sorted(a.items(), key=lambda x: x[1], reverse=True)

arr = []
s = []
for i in a[:5]:
    arr.append(i[0])
    s.append(i[1])
print(sum(s))
arr = sorted(arr, reverse=False)

print(" ".join(map(str, arr)))
