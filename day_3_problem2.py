from bitarray import bitarray

file = open('day_3_test.txt', 'r')
#file = open('day3_1.txt', 'r')

lines = file.readlines()

O2_rate = 0
C02_rate = 0

O2_count = [0 for i in range(len(lines[0]) - 1)]

for line in lines:

    for i in range(len(line)):
        if line[i] == '1':
            O2_count[i] = O2_count[i] + 1
        elif line[i] == '0':
            O2_count[i] = O2_count[i] - 1

print(O2_count)

O2_binary_mask = bitarray('0' * len(O2_count))
C02_binary_mask = bitarray('0' * len(O2_count))

for j in range(len(O2_count)):
    if O2_count[j] > 0:
        O2_binary_mask[j] = 1
        C02_binary_mask[j] = 0
    elif O2_count[j] < 0:
        O2_binary_mask[j] = 0
        C02_binary_mask[j] = 1
    else:
        O2_binary_mask[j] = 1
        C02_binary_mask[j] = 0

print(O2_binary_mask)
print(C02_binary_mask)

#go through the list of binary values, check binary values successively filtering out potential indexes until there is one

def filterValues(binary_mask, possibles):
    possible_indexes = [x for x in range(len(possibles))]
    

    for i in range(len(possibles[0])):
        filter_pass_indexes = []
        for j in possible_indexes:
            if binary_mask[i] == possibles[j][i]:
                filter_pass_indexes.append(j)
        if len(filter_pass_indexes) == 1:
            return possibles[filter_pass_indexes[0]]





O2_binary = filterValues(O2_binary_mask, lines)

C02_binary = filterValues(CO2_binary_mask, lines)


for bit in O2_binary:
    O2_rate = (O2_rate << 1) | bit

for bit in C02_binary:
    C02_rate = (C02_rate << 1) | bit

print("O2 = " + str(O2_rate))

print("C02 = " + str(C02_rate))

print(O2_rate * C02_rate)