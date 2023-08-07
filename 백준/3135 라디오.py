a, b = map(int, input().split())
num = int(input())
arr = []
for _ in range(num):
    arr.append(int(input()))
l = []
l.append(abs(a-b))
for i in arr:
    if i >= b:
        l.append(i-b+1)
    else:
        l.append(b-i+1)
print(min(l))
