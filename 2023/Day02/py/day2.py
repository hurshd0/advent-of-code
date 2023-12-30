import sys
from collections import defaultdict
from functools import reduce
from operator import mul

def read_line(file_path):
    with open(file_path, 'r') as f:
        for line in f:
            yield line.rstrip('\n')
            

# Open the first argument as input or use stdin if no arguments were given
data = read_line(sys.argv[1]) if len(sys.argv) > 1 else sys.stdin


def part_1(data):
    """
    if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
    """
    valid_games = list()
    game_rule = {'red': 12, 'green': 13, 'blue': 14}
    for game in data:
        valid = True
        game_id, game_results = game.split(':')
        game_id = game_id.split(' ')[-1]
        print(f"====================== Game #{game_id} ======================")
        for event in game_results.split(';'):
            print(f"Event: {event}")
            for balls in event.split(','):
                n, color = balls.split()
                if int(n) > game_rule[color]:
                    valid = False
                    break                    
        if valid:
            print("Status: Valid ✅")
            valid_games.append(int(game_id))
        else:
            print("Status: Invalid ❌")      
    print("====================== Summary ======================")
    print(f"Valid games: {valid_games}")
    print(f"Total: {sum(valid_games)}")
    
#part_1(data)

def print_dict(d):
    for k, v in d.items():
        print(f"  {k}: {v}")
    
    
def part_2(data):
    """
    what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
    """
    power_sets = []
    for game in data:
        game_id, game_results = game.split(':')
        game_id = game_id.split(' ')[-1]
        print(f"====================== Game #{game_id} ======================")
        bag = defaultdict(int)
        for event in game_results.split(';'):
            #print(f"Event: {event}")
            for balls in event.split(','):
                n, color = balls.split()
                bag[color] = max(bag[color], int(n))
        print(f"Bag: ")
        print_dict(bag)
        power_set = reduce(mul, bag.values(), 1)
        power_sets.append(power_set)
        print(f"Power Set: {power_set}")
    
    print("====================== Summary ======================")
    print(f"Power Sets: {power_sets}")
    print(f"Total: {sum(power_sets)}") 
    
            
part_2(data)