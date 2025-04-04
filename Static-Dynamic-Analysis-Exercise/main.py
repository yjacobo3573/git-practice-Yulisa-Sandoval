"""This is an example of a program with many costly defects"""

def expensive_op(n):
    """
        Efficiently computes the sum of i * n for i in range(1000) using a formula.

    Args:
        n (int): A multiplier applied to each value from 0 to 999.

    Returns:
        int: The total sum of i * n for i in range(1000).
        """
    return n * (999 * 1000) // 2


def slow_func(lst):
    """
        Runs expensive_op on each index of the input list using list comprehension.

        Args:
            lst (list): Input list (only its length is used).

        Returns:
            list: Results from expensive_op(i) for each index i.
        """
    return [expensive_op(i) for i in range(len(lst))]



def main():
    """
       Executes the main routine by printing done.
       """
    print("Done")
    car=[1,2,3]
    slow_func(car)


if __name__ == "__main__":
    main()
