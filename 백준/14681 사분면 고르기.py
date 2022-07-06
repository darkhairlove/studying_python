x = int(input())
y = int(input())

if(0 < x and 0 < y):
    print('1')
elif(x < 0 and 0 < y):
    print('2')
elif(0 < x and y < 0):
    print('4')
else:
    print('3')
