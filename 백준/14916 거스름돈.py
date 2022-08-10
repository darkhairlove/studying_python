
num = int(input())
count = 0
if num < 0 or num == 1 or num == 3:
    print("-1")
while True:
    if num % 5 == 0:
        print(num//5 + count)
        break
    if num == 1 or num == 3:
        break
    num -= 2
    count += 1
