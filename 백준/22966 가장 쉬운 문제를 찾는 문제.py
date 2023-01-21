num = int(input())
dic = {}
for i in range(num):
    a, b = input().split()
    dic[a] = b

dic = sorted(dic.items(), key=lambda x: x[1])

print(dic[0][0])
