from utils.all import timer, load_grid

@timer
def part1(grid):
    """
    any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)
    """
    HEIGHT = len(grid)
    WIDTH = len(grid[0])

    positions = set()
                 
    for r in range(HEIGHT):
        for c in range(WIDTH):
            # 1. Find symbols
            ch = grid[r][c]
            if ch == '.' or ch.isdigit():
                continue
            # print(f"Found symbol: {ch} at {r},{c}")
            # 2. Find part numbers around the symbol
            for cr in [r -1, r, r + 1]:
                for cc in [c -1, c, c + 1]:
                    # 2a. Check if you are out of bounds or not a digit
                    if cr < 0 or cr >= HEIGHT or cc < 0 or cc >= WIDTH or not grid[cr][cc].isdigit():
                        continue
                    # 2b. Get the part number and add it to positions set
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    positions.add((cr, cc))

    # 3. Extract part numbers from position coordinates
    part_numbers_list = []
    for x, y in positions:
        part_number = ""
        while y < WIDTH and grid[x][y].isdigit():
            part_number += grid[x][y]
            y += 1
        # print(f"Part number: {part_number}")
        part_numbers_list.append(int(part_number))
    return part_numbers_list
    
@timer
def part2(grid):
    """
    
    """
    HEIGHT = len(grid)
    WIDTH = len(grid[0])
    gear_ratios = []
                 
    for r in range(HEIGHT):
        for c in range(WIDTH):
            # 1. Only find '*'
            ch = grid[r][c]
            if ch != '*':
                continue
            # print(f"Found symbol: {ch} at {r},{c}")
            
            # 2. Set positions to empty set
            positions = set()
            
            # 3. Find part numbers around the symbol
            for cr in [r -1, r, r + 1]:
                for cc in [c -1, c, c + 1]:
                    # 3a. Check if you are out of bounds or not a digit
                    if cr < 0 or cr >= HEIGHT or cc < 0 or cc >= WIDTH or not grid[cr][cc].isdigit():
                        continue
                    # 3b. Get the part number and add it to positions set
                    while cc > 0 and grid[cr][cc - 1].isdigit():
                        cc -= 1
                    positions.add((cr, cc))

            if len(positions) != 2:
                continue
            
            # 4. Extract part numbers from position coordinates
            part_numbers = []
            for x, y in positions:
                part_number = ""
                while y < WIDTH and grid[x][y].isdigit():
                    part_number += grid[x][y]
                    y += 1
                # print(f"Part number: {part_number}")
                part_numbers.append(int(part_number))
            gear_ratios.append(part_numbers[0] * part_numbers[1])
    # print(f"Gear ratios: {gear_ratios}")
    return gear_ratios



def main():
    grid = load_grid()
    print("====================== Part 1 ======================")
    part1_result = part1(grid)
    print(f"Result: {sum(part1_result)}")
    print("====================== Part 2 ======================")
    part2_result = part2(grid)
    print(f"Result: {sum(part2_result)}")

if __name__ == "__main__":
    main()