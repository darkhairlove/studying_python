A = int(input())
for i in range(0, A):
    num = list(map(int, input().split()))
    a = num[2] // num[0]
    b = num[2] % num[0]
    if b != 0:
        if a < 9:
            print(str(b)+"0"+str(a + 1))
        else:
            print(str(b)+str(a + 1))
    else:
        if a < 10:
            print(str(num[0])+"0"+str(a))
        else:
            print(str(num[0])+str(a))
