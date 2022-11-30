
num = int(input())
sol = 0
cnt = 0
for i in range(1, num):
    sol = num//i
    if i % 2 == 0:
        if sol > i//2 and sol+(sol+1) * (i // 2) == num:
            cnt += 1
    elif i % 2 != 0:
        if sol * i == num:
            cnt += 1
print(cnt)
#n = int(input())
#cnt = 0
# for i in range(1, n + 1):
#    if i * 2 <= n * 2 - i ** 2 + i and (n * 2 - i ** 2 + i) % (i * 2) == 0:
#        cnt += 1
# print(cnt)
