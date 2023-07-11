a, b = map(str, input().split())

a = int(a)
se_ = set()
for _ in range(a):
    se_.add(input())
if b == 'Y':
    print(len(se_))
elif b == 'F':
    print(len(se_)//2)
elif b == 'O':
    print(len(se_)//3)
