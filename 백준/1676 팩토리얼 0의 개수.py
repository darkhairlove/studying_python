a = int(input())
if a == 0:
    print('0')
elif(0 < a < 501):
    i = 1
    j = 1
    while i < a+1:
        j = j * i
        i += 1
    arr = list(str(j))
    arr.reverse()
    con = 0
    for i in arr:
        if i != '0':
            break
        con += 1
    print(con)
