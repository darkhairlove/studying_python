# 시간 초과

# num = int(input())
# arr2 = []
# for nums in range(1, num+1):
#     arr = []
#     arr.append(nums)
#     for i in range(1, nums//2+1):
#         if nums % i == 0:
#             arr.append(i)
#     arr2.append(sum(arr))
# print(sum(arr2))


# https://www.acmicpc.net/problem/17427
# 참고 블로그
# https: // velog.io/@jaenny/백준-17427-약수의-합2-파이썬python

# 배수를 이용해 푼 문제.
num = int(input())
sum_ = 0
for i in range(1, num+1):
    sum_ += (num//i)*i
print(sum_)
