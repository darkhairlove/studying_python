import sys
input = sys.stdin.readline
a, b = map(int, input().split())
arr = list()
for _ in range(a):
    arr.append(input())
arr.sort()
if b == 0:
    print('{:.2f}'.format(sum(arr)/len(arr)))
    print('{:.2f}'.format(sum(arr)/len(arr)))
else:
    a2 = list(map(float, arr[b:-b]))
    a3 = list(map(float, arr[b:-b]))
    for _ in range(b):
        a3.append(float(arr[b]))
        a3.append(float(arr[-b-1]))
    print('{:.2f}'.format(sum(a2)/len(a2) + 0.00000001))
    print('{:.2f}'.format(sum(a3)/len(a3) + 0.00000001))

# ---- 다른 풀이 ----
input = sys.stdin.readline

N, K = map(int, input().split())
scores = []
for _ in range(N):
    a = float(input())
    scores.append(a)
scores.sort()
if K == 0:
    print('{:.2f}'.format(sum(scores)/len(scores)))
    print('{:.2f}'.format(sum(scores) / len(scores)))
else:
    cut = scores[K:-K]
    corrected = scores.copy()
    for i in range(K):
        corrected[i], corrected[-i-1] = corrected[K], corrected[-K-1]
    print('{:.2f}'.format(sum(cut)/len(cut) + 0.00000001))
    print('{:.2f}'.format(sum(corrected)/len(corrected) + 0.00000001))
