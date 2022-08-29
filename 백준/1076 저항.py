lis = ("black", "brown", "red", "orange", "yellow",
       "green", "blue", "violet", "grey", "white")
l = list()
for i in range(2):
    a = input()
    if a in lis:
        l.append(lis.index(a))
for i in range(1):
    b = input()
    if b in lis:
        h = int(lis.index(b))
a, b = l
print((a*10+b)*10**h)
