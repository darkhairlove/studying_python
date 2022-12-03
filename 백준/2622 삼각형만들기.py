import sys
input = sys.stdin.readline
num = int(input())
cnt = 0

for i in range((num+1)//3, (num+1)//2):
    cnt += (3*i - num + 2)//2

# 시간 초과
#    for j in range(i, num+1):
#        a = num - i - j
#        if i+j > a:  # a < i+j and i < a+j and j < a+i and j <= a:
#            con += 1
#        if j > a:
#            break
print(cnt)
