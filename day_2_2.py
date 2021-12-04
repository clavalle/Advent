file = open('day2_1.txt', 'r')
#file = open('day_2_1_test.txt', 'r')

lines = file.readlines()

aim = 0
x_position = 0
y_position = 0

for instruction in lines:

    parsed_instruction = instruction.split()

    direction = parsed_instruction[0]
    magnitude = int(parsed_instruction[1])

    if direction == 'forward':
        x_position = x_position + magnitude
        y_position = y_position + (aim * magnitude)
    elif direction == 'down':
        aim = aim + magnitude
    elif direction == 'up':
        aim = aim - magnitude

ans = x_position * y_position
print(ans)