import sys
from collections import Counter
input = sys.stdin.readline

num = int(input())
a_list = list()
for _ in range(num):
    a_list.append(int(input()))
print(round(sum(a_list)/num))

a_list.sort()
print(a_list[num//2])

c_list = Counter(a_list).most_common()
if len(c_list) > 1 and c_list[0][1] == c_list[1][1]:
    print(c_list[1][0])
else:
    print(c_list[0][0])

print(max(a_list)-min(a_list))
