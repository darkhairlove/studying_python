n = int(input())
num = []
for _ in range(n):
    num.append(input())

for i in range(1, len(num[0])+1):
    res = []
    for j in range(n):
        if num[j][-i:] in res:
            break
        else:
            res.append(num[j][-i:])
    if len(res) == n:
        print(i)
        break
