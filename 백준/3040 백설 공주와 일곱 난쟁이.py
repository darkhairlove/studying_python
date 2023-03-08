# 9명의 난쟁이의 키를 합한 다음, 차이를 구한 것.
arr = []
for i in range(9):
    arr.append(int(input()))
arr.sort(reverse=False)
ans = sum(arr) - 100
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == ans:
            for k in range(len(arr)):
                if k == j or k == i:
                    pass
                else:
                    print(arr[k])
            exit()
            
# 브루트포스 알고리즘을 사용하여 푼 것

from itertools import combinations
arr = []
for _ in range(9):
    arr.append(int(input()))
    for i in combinations(arr, 7):
        if sum(i) == 100:
            for j in sorted(i):
                print(j)
            break
