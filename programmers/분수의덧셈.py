def solution(denum1, num1, denum2, num2):
    ans = 0
    sol = 0
    if num1 > num2:
        if num1 % num2 == 0:
            sol = num1
            ans = (denum1*num2 + denum2*num1) // num2
        else:
            sol = num1*num2
            ans = denum1*num2 + denum2*num1
    elif num1 < num2:
        if num2 % num1 == 0:
            sol = num2
            ans = (denum1*num2 + denum2*num1) // num1
        else:
            sol = num1*num2
            ans = denum1*num2 + denum2*num1
    else:
        sol = num1
        ans = denum1 + denum2

    for i in range(1, max(sol, ans)+1):
        if sol % i == 0 and ans % i == 0:
            sol1 = sol // i
            ans1 = ans // i

    return [ans1, sol1]
