import os, math

hex_to_bin = { '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

input = ''.join([hex_to_bin[i] for i in open('input.txt', 'r').read()[:-1]])

def decode(index=0, version_sum=0, value_sum=0):
    if all([c == '0' for c in input[index:]]):
        return version_sum, len(input), value_sum
    version = input[index:index+3]
    version_sum += int(version, 2)
    index += 3
    ID = input[index:index+3]
    index += 3
    if int(ID, 2) == 4:
        number = ''
        while True:
            next_5 = input[index:index+5]
            index += 5
            number += next_5[1:]
            if next_5[0] == '0':
                return version_sum, index, int(number, 2)
    else:
        length_type_ID = input[index]
        index += 1
        numbers = []
        if length_type_ID == '0':
            length = int(input[index:index+15],2)
            index += 15
            processed = 0
            while processed < length:
                version_sum, new_index, v = decode(index, version_sum, value_sum)
                numbers.append(v)
                processed += (new_index-index)
                index = new_index
        else:
            n_packets = int(input[index:index+11], 2)
            index += 11
            for i in range(n_packets):
                version_sum, index, v = decode(index, version_sum, value_sum)
                numbers.append(v)
        if os.getenv('part') == 'part2':
            match int(ID, 2):
                case 0: value_sum += sum(numbers)
                case 1: value_sum += math.prod(numbers)
                case 2: value_sum += min(numbers)
                case 3: value_sum += max(numbers)
                case 5: value_sum += 1 if numbers[0] > numbers[1] else 0
                case 6: value_sum += 1 if numbers[0] < numbers[1] else 0
                case 7: value_sum += 1 if numbers[0] == numbers[1] else 0
    return version_sum, index, value_sum

print(decode()) # Returns answer for parts 1 and 2 at index 0 and 2 respectively
