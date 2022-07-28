num1, num2 = input().split()

if '6' in num1 or '6' in num2:
    num1 = num1.replace('6', '5')
    num2 = num2.replace('6', '5')
min_sum = int(num1)+int(num2)
if '5' in num1 or '5' in num2:
    num1 = num1.replace('5', '6')
    num2 = num2.replace('5', '6')
max_sum = int(num1) + int(num2)
print(min_sum, max_sum)
