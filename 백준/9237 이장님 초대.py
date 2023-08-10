num = int(input())

arr = list(map(int, input().split()))
an = []
k = 1
arr = sorted(arr, reverse=True)
for i in arr:
    an.append(i+k)
    k += 1
print(max(an)+1)
