data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# index_keys = [x for x in range(len(data))]
values = [" " for x in range(len(data))]
# draw_check = dict(zip(index_keys, values))

def draw(data):
    # draw_list = []
    peak = 10
    while peak > 0:
        i = 0
        peak -= 1
        while i < len(data):
            # i = 0
            if data[i] == peak:
                values[i] = "X"
                # values = [if data[i] == peak "X" for x else " " for x in values]
                # draw_list.append(values)
            i += 1 
        print("  ".join(values))
        # print
    # for num in range(0, len(data)-1):
        
# print(draw_check)
print(draw(data))