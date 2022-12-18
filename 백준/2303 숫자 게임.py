from itertools import combinations
num = int(input())
a3 = {}
for k in range(num):
    arr = list(map(int, input().split()))
    a2 = list((combinations(arr, 3)))
    for i in a2:
        a3[sum(i)] = (sum(i) % 10, k+1)
    a3_dic = sorted(a3.items(), key=lambda x: x[1], reverse=True)

print(a3_dic[0][1][1])
