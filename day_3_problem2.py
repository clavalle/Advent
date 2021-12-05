from bitarray import bitarray

file = open('day3_1.txt', 'r')

lines = file.readlines()

O2_rate = 0
CO2_rate = 0

#go through the list of binary values, check binary values successively filtering out potential indexes until there is one

def get_binary_value_from_possibles_index(i, possible_indexes, possibles, filter_type):
    
    overall_count = 0
    
    for j in possible_indexes:
        possibles_value = int(possibles[j][i])
        if possibles_value == 1:
            overall_count = overall_count + 1
        elif possibles_value == 0:
            overall_count = overall_count - 1
    if overall_count > 0:
        if filter_type == 'O2':
            return 1
        else:
            return 0
    elif overall_count < 0:
        if filter_type == 'O2':
            return 0
        else:
            return 1
    elif overall_count == 0:
        if filter_type == 'O2':
            return 1
        elif filter_type == 'CO2':
            return 0

def filter_values(filter_type, possibles):
    possible_indexes = [x for x in range(len(possibles))]
    

    for i in range(len(possibles[0])):
        filter_pass_indexes = []
        for j in possible_indexes:
            binary_value = get_binary_value_from_possibles_index(i, possible_indexes, possibles, filter_type)
            possible = int(possibles[j][i])
            if binary_value == possible:
                filter_pass_indexes.append(j)
        if len(filter_pass_indexes) == 1:
            return possibles[filter_pass_indexes[0]].strip()
        possible_indexes = filter_pass_indexes





O2_binary = filter_values('O2', lines)

CO2_binary = filter_values('CO2', lines)


for bit in O2_binary:
    O2_rate = (O2_rate << 1) | int(bit)

for bit in CO2_binary:
    CO2_rate = (CO2_rate << 1) | int(bit)

print("O2 = " + str(O2_rate))

print("CO2 = " + str(CO2_rate))

print(O2_rate * CO2_rate)