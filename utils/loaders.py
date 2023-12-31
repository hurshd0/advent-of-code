import sys
from typing import List
from typing import Iterator, TextIO

def load_by_line() -> Iterator[str]:
    file_input = open(sys.argv[1], "r") if len(sys.argv) > 1 else sys.stdin
    with file_input  as f:
        for line in f:
            yield line.rstrip('\n')
            

def load_grid() -> List[List[str]]:
    file_input = open(sys.argv[1], "r") if len(sys.argv) > 1 else sys.stdin
    grid = []
    with file_input as f:
        grid = [list(line.strip()) for line in f]
    return grid


