home = int(input())
ans = 0
if home % 5 == 0:
    ans = home // 5
elif home > 5:
    ans = 1 + home // 5
elif home < 5:
    ans = 1
print(ans)
