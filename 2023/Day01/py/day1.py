from utils.all import load_by_line

def part1(line):
    digits = [ ch for ch in line if ch.isdigit() ]
    result = 0
    if digits:
        result = int(digits[0] + digits[-1])
    return result

def part2(line):
    numbers = "one two three four five six seven eight nine".split()
    digits = []
    for idx, ch in enumerate(line):
        #print(digits)
        if ch.isdigit():
            digits.append(ch)
            continue
        for num_idx, num in enumerate(numbers):
            if line[idx:].startswith(num):
                digits.append(str(num_idx+1))
    return int(digits[0] + digits[-1])


data = load_by_line()

part1_total = 0
part2_total = 0
for idx, line in enumerate(data):
    #print(f"Reading {idx+1}: {line}")
    part1_calib = part1(line)
    part1_total += part1_calib
    part2_calib = part2(line)
    part2_total += part2_calib
    #print(f"Part 1 Calib. Value {idx+1}: {part1_calib}")
    #print(f"Part 2 Calib. Value {idx+1}: {part2_calib}")
    
print(f"Part 1 Total Calib. Value: {part1_total}")
print(f"Part 2 Total Calib. Value: {part2_total}")