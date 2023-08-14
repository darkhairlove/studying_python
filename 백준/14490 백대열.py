import math
n = input()

a, b = n.split(':')
print(str(int(a)//math.gcd(int(a), int(b))) +
      ':' + str(int(b)//math.gcd(int(a), int(b))))
