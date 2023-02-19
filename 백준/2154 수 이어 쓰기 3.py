
# 시간 초과
# import sys
# input = sys.stdin.readline

# num = int(input())
# arr = ''
# con = 0

# for i in range(1, num+1):

#     arr += str(i)
#     con += len(str(i))
#     if str(num) in arr:
#         print(con-(len(str(num))-1))
#         break

# 정답
s = ""
for i in range(1, 100001):
    s += str(i)

print(s.index(input())+1)
