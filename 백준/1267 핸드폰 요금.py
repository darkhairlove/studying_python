num = int(input())
t = list(map(int, input().split()))
y=0
m=0
for i in t:
    if 30<=i:
        y+=((i//30)+1)*10
        m+=((i//60)+1)*15
    elif i<30:
        y+=10
        m+=15
        

    
if m < y:
    print("M", m)
elif m > y:
    print("Y", y)
else:
    print("Y M", y)
    