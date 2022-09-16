n = int(input())
arr = []
num = 0
while n > 0:
    arr.append(n % 2)
    n //= 2
for i in range(len(arr)):
    if arr[i] == 1:
        num += 3 ** i
print(num)
