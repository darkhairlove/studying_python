num = int(input())

if num == 1:
    print("")
for i in range(2, num+1):
    if num % i == 0:
        while num % i == 0:
            print(i)
            num /= i
