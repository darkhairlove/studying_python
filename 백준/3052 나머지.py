
arr = []
i = 0

for i in range(10):
    arr.append(int(input()) % 42)

result = []
for v in arr:
    if v not in result:
        result.append(v)

print(len(result))
