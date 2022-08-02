
num, a = map(int, input().split())

sum = 0

for i in range(1, num+1):
    if num % i == 0:
        a -= 1
        if a == 0:
            sum = i
print(sum)
