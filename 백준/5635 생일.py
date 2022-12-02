
n = int(input())
data = []

for i in range(0,n):
    data.append(input().split())
    
data.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))

print(data[-1][0])
print(data[0][0])