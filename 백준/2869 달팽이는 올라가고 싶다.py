import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())
print(((v-a-1)//(a-b))+2)
