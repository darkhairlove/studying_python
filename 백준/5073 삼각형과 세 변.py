while 1:
    a, b, c = map(int, input().split())
    lis = []
    lis.append(a)
    lis.append(b)
    lis.append(c)
    a_max = max(lis)
    if a == 0 and b == 0 and c == 0:
        break
    else:
        if sum(lis)-a_max > a_max:
            if a == b == c:
                print('Equilateral')
            elif a == b or c == a or b == c:
                print('Isosceles')
            else:
                print('Scalene')
        else:
            print('Invalid')
