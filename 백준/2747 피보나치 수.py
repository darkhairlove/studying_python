num = int(input())
pi = [0, 1]
for i in range(num-1):
    pi.append(pi[i]+pi[i+1])
print(pi[-1])
