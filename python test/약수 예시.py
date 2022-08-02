num = int(input())

sum = []

for i in range(1, num):
    if num % i == 0:
        sum.append(i)
    i += 1
print(sum)
