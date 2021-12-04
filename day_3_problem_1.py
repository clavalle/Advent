from bitarray import bitarray

#file = open('day_3_test.txt', 'r')
file = open('day3_1.txt', 'r')

lines = file.readlines()

gamma_rate = 0
epsilon_rate = 0

gamma_count = [0 for i in range(len(lines[0]) - 1)]

for line in lines:

    for i in range(len(line)):
        if line[i] == '1':
            gamma_count[i] = gamma_count[i] + 1
        elif line[i] == '0':
            gamma_count[i] = gamma_count[i] - 1

print(gamma_count)

gamma_binary = bitarray('0' * len(gamma_count))
epsilon_binary = bitarray('0' * len(gamma_count))

for j in range(len(gamma_count)):
    if gamma_count[j] > 0:
        gamma_binary[j] = 1
        epsilon_binary[j] = 0
    else:
        gamma_binary[j] = 0
        epsilon_binary[j] = 1

print(gamma_binary)
print(epsilon_binary)


for bit in gamma_binary:
    gamma_rate = (gamma_rate << 1) | bit

for bit in epsilon_binary:
    epsilon_rate = (epsilon_rate << 1) | bit

print("gamma = " + str(gamma_rate))

print("epsilon = " + str(epsilon_rate))

print(gamma_rate * epsilon_rate)