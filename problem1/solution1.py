from typing import List, Tuple
import fileinput

def read_data(seperator: str ="   ") -> Tuple[List[int], List[int]]:
    left, right = [], []

    for line in fileinput.input():
        splitted = line.split(seperator)
        left.append(int(splitted[0]))
        right.append(int(splitted[1]))

    return (left, right)


def main() -> None:
    left, right = read_data()

if __name__ == "__main__":
    main()