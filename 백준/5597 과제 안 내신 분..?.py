ans = list(map(int, range(1, 31)))

for i in range(28):
    num = int(input())
    if num in ans:
        ans.remove(num)
for i in range(len(ans)):
    print(ans[i])
