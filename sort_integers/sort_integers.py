def sort_integers(integers: [int]) -> [int]:
    """
    Returns a new list that contains the elements of integers, but sorted in integer ascending order
    :param integers: a list of integers to sort
    :return: a new list of integers, sorted in ascending order
    """
    integers = [*integers]
    n = len(integers)
    for i in range(n - 1):  # loop through the list
        for j in range(0, n - i - 1):  # assume inductively that the final i elements are sorted
            # Swap if current element is > next element
            if integers[j] > integers[j + 1]:
                integers[j], integers[j + 1] = integers[j + 1], integers[j]
    return integers

