arr = input()
b = len(arr) % 10
a = []
c = 0
for i in arr:
    a.append(i)
    if 10 == len(a):
        c += 1
        print("".join(a))
        a = []
    elif c == len(arr)//10 and len(a) == b:
        print("".join(a))
