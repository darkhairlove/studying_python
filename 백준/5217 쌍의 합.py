n = int(input())
for i in range(n):
    s = 1
    num = int(input())
    print("Pairs for %d:" % num, end=' ')

    for k in range((num-1)//2):
        if k != 0:
            print(',', end=' ')
        print(s, num - s, end='')
        s += 1

    print()
