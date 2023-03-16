num = int(input())
arr = list(map(int, input().split()))

s1 = sorted(arr)
s2 = sorted(arr, reverse=True)

new_arr = []
for i in range(len(arr)):
    x = s1[i]+s2[i]
    new_arr.append(x)
print(min(new_arr))
