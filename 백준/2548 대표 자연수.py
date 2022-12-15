
# 시간초과
# num =int(input())
# arr1= list()
# arr2= list()
# arr = list(sorted(map(int, input().split())))

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         arr1.append(abs(arr[i]-arr[j]))
    
#     arr2.append(sum(arr1))
#     arr1 = list()

# a=arr2.index(min(arr2))

# print(arr[a])
# 중앙값으로 풀기
num =int(input())
arr = list(map(int, input().split()))
arr.sort()
if len(arr) % 2 ==0:
    print(arr[len(arr)//2-1])
else:
    print(arr[len(arr)//2])
    