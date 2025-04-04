"""This is an example of a program with many costly defects"""

import math
import random


def expensive_op(n):
    """
        Performs a computationally expensive operation by summing i * n for i in range(1000).

        Args:
            n (int): A multiplier applied to each value from 0 to 999.

        Returns:
            int: The total sum of i * n for i in range(1000).
        """
    total = 0
    for i in range(1000):
        total += i * n
    return total


def slow_func(lst):
    """
       Runs expensive_op on each index of the input list.

       Args:
           lst (list): Input list (only length is used).

       Returns:
           list: Results from expensive_op(i) for each index i.
       """
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result


def unused_function():
    """
        Adds two numbers and returns the result.

        Returns:
            int: The sum of 10 and 20.
        """
    x = 10
    y = 20
    z = x + y
    return z


def main():
    """
       Executes the main routine by running slow_func on a list of 1000 numbers.
       """
    print("Done")


if __name__ == "__main__":
    main()
