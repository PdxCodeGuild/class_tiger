data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
values = [" " for x in range(len(data))]

def draw(data):
    peak = 10
    while peak > 1:
        i = 0
        peak -= 1
        while i < len(data):
            if data[i] == peak:
                values[i] = "X"
            i += 1 
        print("  ".join(values))
print(draw(data))
