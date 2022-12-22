# 메모리 초과
# num = int(input())
# arr = list()
# for i in range(1, num+1):
#     arr.append(str(i))
# print(len(''.join(arr)))

# https://www.acmicpc.net/problem/1748
# 성공
num = int(input())
so = 0
l = len(str(num))
con = len(str(num))-1
for i in range(1, l):
    so += 9*(10**(i-1))*i
so += (num-(10**con)+1)*l
print(so)
