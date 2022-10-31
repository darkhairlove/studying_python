a, b = map(int, input().split())

arr_a = set(map(int, input().split()))
arr_b = set(map(int, input().split()))
se = list(arr_a-arr_b)
print(len(arr_a-arr_b))
se.sort()
for i in se:
    print(i, end=' ')
