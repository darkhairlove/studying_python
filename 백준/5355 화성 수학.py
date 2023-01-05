# https: // www.acmicpc.net/problem/5355
num = int(input())

arr2 = ['#', '%', '@']
for i in range(num):
    arr = []
    a = input()
    a = a.split()
    som = float(a[0])
    for i in a:
        if i in arr2:
            if i == '@':
                som *= 3
            elif i == '%':
                som += 5
            elif i == '#':
                som -= 7

    print("%0.2f" % som)
