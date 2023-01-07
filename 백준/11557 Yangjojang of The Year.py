num = int(input())

for _ in range(num):
    a = int(input())
    dic = {}
    for _ in range(a):
        sc = input().split()
        dic[sc[0]] = int(sc[1])
        sorted_dict = sorted(
            dic.items(), key=lambda item: item[1], reverse=True)
    print(sorted_dict[0][0])
