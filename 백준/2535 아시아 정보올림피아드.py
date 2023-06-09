num = int(input())
dic = {}
for i in range(num):
    a, b, c = map(int, input().split())
    dic[c] = (a, b)

dic = sorted(dic.items(), reverse=True)


for i in range(len(dic)):
    if dic[1][1][0] == dic[0][1][0] and dic[1][1][0] == dic[2][1][0]:
        if dic[i][1][0] != dic[1][1][0]:
            print(dic[0][1][0], dic[0][1][1])
            print(dic[1][1][0], dic[1][1][1])
            print(dic[i][1][0], dic[i][1][1])
            break
        else:
            continue
    else:
        print(dic[0][1][0], dic[0][1][1])
        print(dic[1][1][0], dic[1][1][1])
        print(dic[2][1][0], dic[2][1][1])
        break
