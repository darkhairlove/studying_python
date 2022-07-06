A, B, C = map(int, input().split())

if(A == B == C):
    print(10000 + A*1000)
elif(A == B and B != C):
    print(1000 + A*100)
elif(A == C and A != B):
    print(1000 + A*100)
elif(B == C and A != C):
    print(1000 + B*100)
else:
    D = max(A, B, C)
    print(D*100)
