num = int(input())
dic = {}
con = 0
for i in range(num):
    a, b = map(int, input().split())
    if a not in dic:
        dic[a] = b
    else:
        if dic[a] != b:
            con += 1
            dic[a] = b
print(con)
