num = int(input())
arr = list()
for i in range(num):
    arr.append(input())
a = arr.count('0')
b = arr.count('1')
if a < b:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
