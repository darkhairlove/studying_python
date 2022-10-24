N, K = map(int, input().split())

arr = list(map(int, input().split()))
sum2 = sum(arr[:K])
res = [sum2]
for i in range(0, len(arr)-K):
    sum2 = sum2 - arr[i] + arr[i+K]
    res.append(sum2)
print(max(res))
