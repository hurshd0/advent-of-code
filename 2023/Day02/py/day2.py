import sys
from collections import defaultdict
from functools import reduce
from operator import mul
from utils.all import *


@timer
def part1(data):
    """
    if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes
    """
    valid_games = list()
    game_rule = {'red': 12, 'green': 13, 'blue': 14}
    for game in data:
        valid = True
        game_id, game_results = game.split(':')
        game_id = game_id.split(' ')[-1]
        # print(f"Game #{game_id}")
        for event in game_results.split(';'):
            # print(f"Event: {event}")
            for balls in event.split(','):
                n, color = balls.split()
                if int(n) > game_rule[color]:
                    valid = False
                    break                    
        if valid:
            # print("Status: Valid ✅")
            valid_games.append(int(game_id))
        else:
            pass
            # print("Status: Invalid ❌")      
    return valid_games
    

@timer
def part2(data):
    """
    what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
    """
    power_sets = []
    for game in data:
        game_id, game_results = game.split(':')
        game_id = game_id.split(' ')[-1]
        # print(f"Game #{game_id}")
        bag = defaultdict(int)
        for event in game_results.split(';'):
            # print(f"Event: {event}")
            for balls in event.split(','):
                n, color = balls.split()
                bag[color] = max(bag[color], int(n))
        # print(f"Bag: ")
        # print_dict(bag)
        power_set = reduce(mul, bag.values(), 1)
        power_sets.append(power_set)
        # print(f"Power Set: {power_set}")
    return power_sets
    


def main():
    print("====================== Part 1 ======================")
    part1_valid_games = part1(load_by_line())
    # print(f"Valid games: {part1_valid_games}")
    print(f"Total: {sum(part1_valid_games)}")

    print("====================== Part 2 ======================")
    part2_power_sets = part2(load_by_line())
    # print(f"Power Sets: {part2_power_sets}")
    print(f"Total: {sum(part2_power_sets)}") 
    
if __name__ == "__main__":
    main()