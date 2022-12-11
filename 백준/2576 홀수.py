arr = list()
for i in range(7):
    arr.append(int(input()))
so = list()
for i in arr:
    if i % 2 != 0:
        so.append(i)
if len(so) > 0:
    print(sum(so))
    print(min(so))
else:
    print(-1)
