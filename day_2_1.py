file = open('day2_1.txt', 'r')

lines = file.readlines()

x_position = 0
y_position = 0

for instruction in lines:

    parsed_instruction = instruction.split()

    direction = parsed_instruction[0]
    magnitude = int(parsed_instruction[1])

    if direction == 'forward':
        x_position = x_position + magnitude
    elif direction == 'down':
        y_position = y_position + magnitude
    elif direction == 'up':
        y_position = y_position - magnitude

ans = x_position * y_position
print(ans)
        
