
#sum1 = 0
#a, b = map(list, input().split())
#a = list(map(int, a))
#b = list(map(int, b))
# for i in range(len(a)):
#    sum1 += int(a[i])
#sum2 = 0
# for j in range(len(b)):
#    sum2 += sum1*int(b[j])
#print(sum(a) * sum(b))


import sys
input = sys.stdin.readline
a, b = map(list, input().split())
a = list(map(int, a))
b = list(map(int, b))
print(sum(a) * sum(b))
