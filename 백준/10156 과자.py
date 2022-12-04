a, b, c = map(int, input().split())
sol =  a * b
if sol - c<= 0:
    print(0)
else:
    print(abs(c-sol))
    