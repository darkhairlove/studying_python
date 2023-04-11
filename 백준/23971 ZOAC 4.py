from math import ceil

h, w, n, m = map(int, input().split())

a = ceil(h/(n+1))
b = ceil(w/(m+1))
print(a*b)
