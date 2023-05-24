num = int(input())
dic = {}
dic2 = {}
dic[1] = 0
dic[2] = 0
dic[3] = 0
dic2[1] = 0
dic2[2] = 0
dic2[3] = 0
for i in range(num):
    a, b, c = map(int, input().split())
    dic[1] += a
    dic[2] += b
    dic[3] += c
    dic2[1] += a**2
    dic2[2] += b**2
    dic2[3] += c**2
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
dic2 = sorted(dic2.items(), key=lambda x: x[1], reverse=True)

if dic[0][1] == dic[1][1] and dic[0][1] != dic[2][1]:
    if dic2[0][1] != dic2[1][1]:
        print(dic2[0][0], dic[0][1])
    else:
        print(0, dic[0][1])
elif dic[0][1] == dic[1][1] and dic[0][1] == dic[2][1]:
    if dic2[0][1] != dic2[1][1]:
        print(dic2[0][0], dic[0][1])
    else:
        print(0, dic[0][1])
else:
    print(dic[0][0], dic[0][1])
