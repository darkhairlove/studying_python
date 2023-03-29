num = int(input())
arr1 = []
arr2 = []
for i in range(num):
    a, b = map(int, input().split())
    arr1.append(a)
    arr2.append(b)
if num == 1:
    print(0)
else:
    x = max(arr1) - min(arr1)
    y = max(arr2) - min(arr2)
    print(x*y)
