day = 0
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
a, b = map(int, input().split())

for i in range(a-1):
    day += month[i]

day = (day+b) % 7

print(week[day])
