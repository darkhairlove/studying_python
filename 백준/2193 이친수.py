# https://www.acmicpc.net/problem/2193
num = int(input())
pi = [0, 1]
for i in range(num-1):
    pi.append(pi[i]+pi[i+1])
print(pi[-1])


# 끝의 자리가 1인 수 개수는 이전 0의 개수와 같고
# 0의개수는 그 전 수의 개수를 더함
# 즉 피보나치 수열
