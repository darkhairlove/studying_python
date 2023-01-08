num = int(input())
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
for i in range(num):
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        s1 += 1
    elif a > 0 and b < 0:
        s4 += 1
    elif a < 0 and b > 0:
        s2 += 1
    elif a < 0 and b < 0:
        s3 += 1
    elif a == 0 or b == 0:
        s5 += 1
print("Q1:", s1)
print("Q2:", s2)
print("Q3:", s3)
print("Q4:", s4)
print("AXIS:", s5)
