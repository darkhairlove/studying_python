num = int(input())

for _ in range(num):
    a = int(input())
    dic = {}
    for _ in range(a):
        x, y = input().split()
        dic[y] = int(x)
    dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    print(dic[0][0])
