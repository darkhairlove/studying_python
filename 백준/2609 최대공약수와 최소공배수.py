a, b = map(int, input().split())


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def lcd(a, b):
    return (a * b)//gcd(a, b)


print(gcd(a, b))
print(lcd(a, b))
