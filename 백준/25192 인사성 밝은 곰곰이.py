num = int(input())
dic = {}
arr = []
ans = 0
for i in range(num):
    arr.append(input())
for i in arr:
    if i == 'ENTER':
        ans += sum(dic.values())
        dic = {}
    else:
        dic[i] = 1
ans += sum(dic.values())

print(ans)
