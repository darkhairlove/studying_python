import math
num1 = int(input())
num2 = int(input())
n1 = math.ceil(num1**(1/2))
n2 = int(num2**(1/2))
arr = list()
for i in range(n1, n2+1):
    arr.append(i ** 2)
if len(arr) != 0:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)
