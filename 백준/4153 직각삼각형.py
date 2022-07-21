while 1:
    num = list(map(int, input().split()))
    num = sorted(num, reverse=False)
    if num[0] == 0 and num[1] == 0 and num[2] == 0:
        break
    if num[0]*num[0] + num[1]*num[1] == num[2]*num[2]:
        print("right")
    else:
        print("wrong")
