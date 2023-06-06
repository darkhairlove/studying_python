z = [1, 0, 1]
o = [0, 1, 1]


def fib(a):
    l = len(z)
    if a >= l:
        for i in range(l, a+1):
            z.append(z[i-1]+z[i-2])
            o.append(o[i-1]+o[i-2])
    print('{} {}'.format(z[a], o[a]))


num = int(input())

for _ in range(num):

    a = int(input())
    fib(a)
