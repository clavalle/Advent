file = open('depth.txt', 'r')

lines = file.readlines()

prev = None
inc_count = 0

record_total = len(lines)
print(record_total)
window_size = 3

def sumWindow(value_array, current_index, window_size):
    total = 0
    for j in range(window_size):
        if current_index == 0:
            print(value_array[current_index + j])
        total = total + int(value_array[current_index + j])
    
    return total

for i in range(record_total - window_size + 1):

    current_window_depth = sumWindow(lines, i, window_size)

    if prev is None:
        prev = current_window_depth
        continue
    if current_window_depth > prev:
        inc_count = inc_count + 1
    prev = current_window_depth

print(inc_count)
