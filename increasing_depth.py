file = open('depth.txt', 'r')

lines = file.readlines()

prev = None
inc_count = 0

for depth in lines:
    print(depth)
    if prev is None:
        prev = int(depth)
        continue
    if int(depth) > prev:
        print('increasing')
        inc_count = inc_count + 1
    prev = int(depth)

print(inc_count)