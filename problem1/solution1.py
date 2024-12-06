from typing import List, Tuple
import fileinput

# Run program with the command "python solution1.py < input.txt"

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


def main() -> None:
    left, right = read_data()



if __name__ == "__main__":
    main()