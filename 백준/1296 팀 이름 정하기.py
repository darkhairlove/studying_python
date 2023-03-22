name = input()

num = int(input())
arr = []
for _ in range(num):
    arr.append(input())
dic = {}
for i in arr:
    o1 = i.count('L') + name.count('L')
    o2 = i.count('O') + name.count('O')
    o3 = i.count('V')+name.count('V')
    o4 = i.count('E')+name.count('E')
    dic[i] = ((o1+o2)*(o1+o3)*(o1+o4)*(o2+o4)*(o2+o3)*(o3+o4)) % 100
dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]), reverse=False)
print(dic[0][0])
