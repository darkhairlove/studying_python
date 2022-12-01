a, b = map(int, input().split())

if a < b:
    print(b-a-1)
    for i in range(a+1, b):
        print(i)
elif a > b:
    print(a-b-1)
    for i in range(b+1, a):
        print(i)
else:
    print(0)
    
    