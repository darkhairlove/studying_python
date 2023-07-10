from collections import Counter

num = int(input())
dic = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for _ in range(num):
    sum1 = 0
    con = 0
    arr = input()
    ls = arr.split(' ')
    for i in ls:
        cn = Counter(i)
        sum1 += len(i)
        for k in dic:
            con += cn[k]
    print(sum1-con, con)
