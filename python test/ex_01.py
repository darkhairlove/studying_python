def swap_reference(ex, offset_x, offset_y):
    temp = ex[offset_x] 
    ex[offset_x] = ex[offset_y]
    ex[offset_y] = temp


ex = [1, 2, 3, 4, 5]
swap_reference(ex, 0, 3)
print(ex)
