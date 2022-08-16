import sys
input = sys.stdin.readline

num = int(input())
count = 0

while True:
    if num % 5 == 0:
        print(num//5 + count)
        break
    if num == 1 or num == 2:
        break
    num -= 3
    count += 1
if num < 0 or num == 1:
    print("-1")
