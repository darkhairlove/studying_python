num = int(input())
arr = []
for _ in range(num):
    a, b = map(int, input().split())
    arr.append(b % a)
print(sum(arr))
