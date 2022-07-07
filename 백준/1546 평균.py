N = int(input())
score = list(map(int, input().split()))

arr = []
i = 0
j = 0
m = max(score)
for i in range(N):
    arr.append((int(score[i])/m) * 100)
for j in arr:
    A = sum(arr)/N
print(A)
