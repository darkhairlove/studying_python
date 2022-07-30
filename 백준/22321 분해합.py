num = int(input())

result = 0
for i in range(1, num+1):
    A = list(map(int, str(i)))
    result = i + sum(A)
    if result == num:
        print(i)
        break
    if i == num:
        print(0)
