num = int(input())
sol = num
j = 1
con = 0
while True:
    if sol >= j:
        sol -= j
        j += 1
        con += 1
    elif sol <= 0:
        break
    else:
        j = 1
print(con)
