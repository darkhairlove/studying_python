num = int(input())
arr = list()
for _ in range(num):
    arr.append(int(input()))
sum_ = sum(arr)//2
for i in range(num):
    ans = 0
    for j in range(1, num, 2):
        ans += arr[(i+j) % num]
    print(sum_ - ans)
