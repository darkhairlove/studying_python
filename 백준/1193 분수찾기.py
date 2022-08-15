num = int(input())
line = 0
end = 0
while num > end:
    line += 1
    end += line
nums = end-num
if line % 2 == 0:
    top = line - nums
    bot = nums + 1
else:
    top = nums + 1
    bot = line - nums
print(str(top)+"/"+str(bot))
