num = int(input())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))

s = 0
for i in range(num):
    s += min(a_arr) * max(b_arr)
    a_arr.pop(a_arr.index(min(a_arr)))
    b_arr.pop(b_arr.index(max(b_arr)))
print(s)
