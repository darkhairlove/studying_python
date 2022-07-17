n, k = list(map(int, input().split()))

num2 = list(map(int, input().split()))

num2.sort(reverse=True)
print(num2[k-1])
