
def join(*lists: list, sep: str = '-') -> list or None:
    """
    The function returns one list consisting of all the lists obtained as parameters.
    If the sep parameter is provided, it should be threaded as an element between any two lists.
    If not provided, the character "-" should be threaded in place.
    @param lists: Unlimited number of lists, each list as a parameter.
    @param sep: The character threaded between the lists.
    @return: List of chained lists or None in case we did not get lists as parameters.
    """
    new_list = []
    for x in range(len(lists) - 1):
        new_list = new_list + lists[x] + [sep]
    if lists:
        new_list = new_list + lists[-1]
        return new_list
    return None


"""
An example usage:
join([1, 2], [8], [9, 5, 6], sep='@')
>>> [1, 2, '@', 8, '@', 9, 5, 6]
"""
