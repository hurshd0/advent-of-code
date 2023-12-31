from utils.all import load_by_line
import collections

Card = collections.namedtuple("Card", ["id", "winning", "have"])
    
    
def _parse_card(line):
    card_str, nums_str = line.split(": ")
    _, card_id = card_str.split()
    card_id = int(card_id)
    assert _ == "Card"
    winning_str, have_str = nums_str.split(" | ")
    winning = set([int(x) for x in winning_str.split()])
    have = set([int(x) for x in have_str.split()])
    return Card(id=card_id, winning=winning, have=have)
    
def _get_matches(data):
    matches = []
    for line in data:
        card = _parse_card(line)
        matched = card.have & card.winning
        matches.append(len(matched))
        # print(f"Card #{card.id}: Matched: {matched}, Count: {len(matched)}")
    return matches


def part1(data):
    matches = _get_matches(data)
    points = [2**(n-1) if n > 0 else 0 for n in matches]
    return points

def part2(data):
    matches = _get_matches(data)
    counts = [1] * len(matches)
    for i, n in enumerate(matches):
        for j in range(n):
            counts[i + j + 1] += counts[i]
    return counts


def main():
    print("====================== Part 1 ======================")
    data = load_by_line()
    part1_result = part1(data)
    print(f"Points: {part1_result}")
    print(f"Result: {sum(part1_result)}")
    print("====================== Part 2 ======================")
    data = load_by_line()
    part2_result = part2(data)
    print(f"Instances: {part2_result}")
    print(f"Result: {sum(part2_result)}")

if __name__ == "__main__":
    main()