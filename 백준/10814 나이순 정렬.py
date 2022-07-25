num = int(input())
arr = []
for i in range(num):
    age, name = map(str, input().split())
    age = int(age)
    arr.append((age, name))
arr.sort(key=lambda name: name[0])

for i in arr:
    print(i[0], i[1])
