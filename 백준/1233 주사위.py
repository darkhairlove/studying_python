import collections
a, b, c = map(int, input().split())
li = list()
res = list()
for i in range(1, a+1):
    li.append(i)
    for j in range(1, b+1):
        li.append(j)
        for k in range(1, c+1):
            li.append(k)
            res.append(sum(li))
            li.pop(-1)
        li.pop(-1)
    li.pop(-1)
res2 = collections.Counter(res)

print(res2.most_common(1)[0][0])
