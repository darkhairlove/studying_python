a = int(input())

if a == 0:
    print('1')
elif(0 < a < 13):
    for i in range(a):
        print(i*(i-1))
