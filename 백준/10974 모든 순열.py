from itertools import permutations
num = int(input())
arr = []
for a in range(1, num+1):
    arr.append(a)
result = list(permutations(arr, num))  # 모든 순열 구하기
for i in result:
    for a in i:
        print(a, end=' ')
    print()
