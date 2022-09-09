num = int(input())
a = list(map(int, input().split()))


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


for i in range(1, num):
    g = gcd(a[0], a[i])
    print('{0}/{1}'.format(a[0]//g, a[i]//g))
