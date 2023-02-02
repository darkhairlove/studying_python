num = int(input())

for _ in range(num):
    a = int(input())
    wear = {}
    for _ in range(a):
        j_, k_ = input().split()
        if k_ not in wear:
            wear[k_] = [j_]
        else:
            wear[k_] += [j_]
    s_ = 1
    for i in wear.items():
        s_ *= len(i[1])+1
    print(s_-1)
