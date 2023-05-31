num = int(input())
a = []
a1 = []
dic = {}
con = 0
pr = 0
for i in range(num):
    a.append(int(input()))
for i in a:
    dic[con] = i
    con += 1
arr = sorted(dic.items(), reverse=True)
for i in arr:
    a1.append(i[1])
for i in range(len(a1)-1):
    while True:
        if a1[i] <= a1[i+1]:
            a1[i+1] -= 1
            pr += 1
        else:
            break
print(pr)
