num = int(input())
a = int(input())
sum = 0
for i in range(a):
    c, d = map(int, input().split())
    sum += c*d
if num == sum:
    print("Yes")
else:
    print("No")
