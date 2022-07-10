
num = list(input())
num.reverse()
ans = 0
for i in num:
    if num[0] > num[4]:
        ans += 1
    elif num[0] == num[4]:
        if num[1] > num[5]:
            ans += 1
        elif num[1] == num[5]:
            if num[2] > num[6]:
                ans += 1

if ans == 7:
    print(num[0]+num[1]+num[2])
else:
    print(num[4]+num[5]+num[6])
