num = int(input())
rgb = []
for _ in range(num):
    rgb.append(list(map(int, input().split())))

for i in range(1, num):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]

    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]

    rgb[i][2] = min(rgb[i-1][1], rgb[i-1][0]) + rgb[i][2]
print(min(rgb[-1]))
