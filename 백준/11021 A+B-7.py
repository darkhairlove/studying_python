N = int(input())
i = 1
for i in range(N):

    a, b = map(int, input().split())

    print('Case', '#'+str(i+1)+':', a+b)
