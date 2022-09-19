num = int(input())
arr = []
for i in range(num):
    n = int(input())
    if n == 0:
        arr.pop()
    else:
        arr.append(n)
print(sum(arr))
