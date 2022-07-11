
arr = input()
arr = arr.upper()
res = []
j = 65
for i in range(26):
    if chr(j) in arr:
        res.append(arr.count(chr(j)))
    else:
        res.append(-1)
    j += 1
sum = 0
a = 0
ans = []
for i in res:
    if res[a] == max(res):
        sum += 1
        ans.append(a)
    a += 1
if sum == 1:
    print(chr(ans[0]+65))
elif sum > 1:
    print("?")
