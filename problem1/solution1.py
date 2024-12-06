from typing import List, Tuple
import fileinput

# Advent of code December 1, 2024
# Run the program with the command "python solution1.py < input.txt"

def read_data(separator: str ="   ") -> Tuple[List[int], List[int]]:
    '''
    Reads input from a file with two columns of integers, separated with a specified string.

    Args:
        separator (str): The string that separates the columns (defaults to three spaces).
    
    Returns:
        Tuple[List[int], List[int]]: A tuple with the two corredsponding lists.

    '''
    left, right = [], []

    for line in fileinput.input():
        splitted = line.split(separator)
        left.append(int(splitted[0]))
        right.append(int(splitted[1]))

    return (left, right)


def solve(left: List[int], right: List[int]) -> int:
    '''
    Solves the problem (see problem description),
    i.e. calculates the difference between each element in the corresponding lists
    after having been sorted.

    Args:
        left (List[int]): the left input list.
        right (List[int]): the right input list.
    
    Returns:
        int: the difference.
    '''

    left.sort()
    right.sort()

    zipped = zip(left, right)
    func = lambda x: abs(x[0] - x[1])

    differences = map(func, zipped)
    return sum(differences)


def main() -> None:
    left, right = read_data()
    solution = solve(left, right)
    print(solution)


if __name__ == "__main__":
    main()