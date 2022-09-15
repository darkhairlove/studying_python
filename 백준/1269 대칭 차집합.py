a, b = map(int, input().split())
c = set(map(int, input().split()))
e = set(map(int, input().split()))
print((len(c-e))+(len(e-c)))
