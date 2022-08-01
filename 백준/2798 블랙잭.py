a, b = map(int, input().split())
num = list(map(int, input().split()))
res = set()
i = 0
while i < a-2:
    j = i+1
    while j < a-1:
        k = j+1
        while k < a:
            if num[i]+num[j]+num[k] <= b:
                res.add(num[i]+num[j]+num[k])
            k += 1
        j += 1
    i += 1
print(max(res))
