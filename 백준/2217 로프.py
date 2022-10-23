num = int(input())
arr = []
for _ in range(num):
    arr.append(int(input()))
arr.sort(reverse=True)
sol = []
for j in range(num):
    sol.append(arr[j]*(j+1))
print(max(sol))
