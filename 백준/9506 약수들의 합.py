while True:
    num = int(input())
    arr = list()
    for i in range(1, num//2+1):
        if num % i == 0:
            arr.append(i)
    if sum(arr) == num:
        res = ' + '.join(map(str, arr))
        print(str(num) + ' = ' + res)
    elif num != -1 and sum(arr) != num:
        print(str(num) + ' is NOT perfect.')

    if num == -1:
        break
