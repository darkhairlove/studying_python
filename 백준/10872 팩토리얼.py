a = int(input())

if a == 0:
    print('1')
elif(0 < a < 13):
    i = 1
    j = 1
    while i < a+1:
        j = j * i
        i += 1
    print(j)
