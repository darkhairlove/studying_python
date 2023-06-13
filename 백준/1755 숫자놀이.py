dic = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
       5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
dic2 = {}
n, b = map(int, input().split())
arr = []
for i in range(n, b+1):
    arr.append(i)

for i in arr:
    a = [int(k) for k in str(i)]
    dic2[i] = ''
    for j in a:
        if j in dic.keys():
            dic2[i] += dic[j]+" "
dic2 = sorted(dic2.items(), key=lambda x: x[1], reverse=False)
arr2 = []
for i in dic2:
    arr2.append(str(i[0]))

for i in range((b-n+1)//10+1):
    print(" ".join(arr2[10*i:10*(i+1)]))
