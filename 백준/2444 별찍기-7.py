num = int(input())
son = 2*(num//2)+num

for i in range(num-1):
    for j in range(1, son+1):
        if num-i > j:
            print(" ", end='')
        elif num-i <= j <= num+i:
            print("*", end='')
    print()

i = num-1
for _ in range(num):
    for j in range(1, son+1):
        if num-i > j:
            print(" ", end='')
        elif num-i <= j <= num+i:
            print("*", end='')
    i -= 1
    print()
