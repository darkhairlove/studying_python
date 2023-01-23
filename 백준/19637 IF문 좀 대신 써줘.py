# 이분 탐색 문제
# https://www.acmicpc.net/problem/19637
import sys
input = sys.stdin.readline
n1, n2 = map(int, input().split())
nam_ = []
pow_ = []
for _ in range(n1):
    a, b = input().split()
    b = int(b)
    if pow_ and pow_[-1] == b:  # 가장 처음 칭호만 저장해주기 위해
        continue
    nam_.append(a)
    pow_.append(b)


def binary_search(p):
    left = 0
    right = len(pow_) - 1
    while left <= right:
        mid = (left + right) // 2
        if p > pow_[mid]:
            left = mid + 1
        else:
            right = mid - 1
    print(nam_[right+1])


for _ in range(n2):
    n_ = int(input())
    binary_search(n_)
