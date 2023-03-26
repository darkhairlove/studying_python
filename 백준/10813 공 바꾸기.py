a, b = map(int, input().split())
dic = {}
for i in range(1, a+1):
    dic[i] = i
for _ in range(b):
    c, d = map(int, input().split())
    last_c = dic.get(c)
    dic[c] = dic.get(d)
    dic[d] = last_c
a = list(dic.values())
for i in a:
    print(i)
