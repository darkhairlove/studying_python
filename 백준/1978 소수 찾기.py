
def is_prime_number(x):
    if x == 1:
        return False
    i = 2
    while i < x:
        if x % i == 0:
            return False
        i += 1
    return True


t = int(input())
a = set(map(int, input().split()))
sum = 0
for x in a:
    if is_prime_number(x):
        sum += 1
print(sum)
