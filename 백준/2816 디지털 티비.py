n = int(input())

ch = [input() for _ in range(n)]
i1, i2 = ch.index('KBS1'), ch.index('KBS2')

if i1 > i2:
    i2 += 1
print('1'*i1+'4'*i1+'1'*i2+'4'*(i2-1))
