
sum = 1
num = list(input())
a = len(num)-1
for i in range(len(num)//2):
    if num[i] == num[a-i]:
        sum = 1
    else:
        sum = 0
        break

if sum == 1:
    print("1")
else:
    print("0")
