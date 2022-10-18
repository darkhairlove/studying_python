
num = int(input())

d = [0, 1]
for i in range(2, abs(num)+1):

    d.append((d[i-1] + d[i-2]) % 1000000000)
if num % 2 == 0 and num < 0:
    print(-1)
elif num == 0:
    print(0)
else:
    print(1)
print(d[abs(num)])
