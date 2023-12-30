import sys

def read_line(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.rstrip('\n')
            

# Open the first argument as input or use stdin if no arguments were given
data = read_line(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin


def part_1(line):
    digits = [ ch for ch in line if ch.isdigit() ]
    return int(digits[0] + digits[-1])

def part_2(line):
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



total = 0
for idx, line in enumerate(data):
    #print(f"Reading {idx+1}: {line}")
    calib_val = part_2(line)
    #print(f"Calibration Value {idx+1}: {calib_val}")
    total += calib_val
    
print(f'Total Calibration Value: {total}')
        