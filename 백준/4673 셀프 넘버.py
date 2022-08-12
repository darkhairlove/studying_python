num = set(range(1, 10001))
hnum = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    hnum.add(i)
self_num = sorted(num-hnum)
for i in self_num:
    print(i)
