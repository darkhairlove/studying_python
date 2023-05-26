a, b = map(int, input().split())
dic = {}
for _ in range(a):
    c, d = map(str, input().split())
    dic[c] = d

for _ in range(b):
    name = input()
    print(dic[name])
