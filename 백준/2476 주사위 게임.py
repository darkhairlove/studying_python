num = int(input())
arr = list()
for i in range(num):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        arr.append(10000+a*1000)
    elif a == b and a != c:
        arr.append(1000+a*100)
    elif a == c and a != b:
        arr.append(1000+a*100)
    elif b == c and a != b:
        arr.append(1000+b*100)
    elif a > b > c or a > c > b:
        arr.append(a*100)
    elif b > a > c or b > c > a:
        arr.append(b*100)
    elif c > a > b or c > b > a:
        arr.append(c*100)
print(max(arr))
