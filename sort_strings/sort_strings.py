def sort_strings(strings: [str]) -> [str]:
    """
    Returns a new list that contains the elements of strings, but sorted in string ascending order
    :param strings: a list of strings to sort
    :return: a new list of strings, sorted in ascending order
    """
    strings = [*strings]
    n = len(strings)
    for i in range(n - 1):  # loop through the list
        for j in range(0, n - i - 1):  # assume inductively that the final i elements are sorted
            # Swap if current element is > next element
            if strings[j] > strings[j + 1]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings
