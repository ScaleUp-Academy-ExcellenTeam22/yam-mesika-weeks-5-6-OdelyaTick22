def join(*lists, sep='-'):
    l = []
    for x in range(len(lists) - 1):
        l = l + lists[x] + [sep]
    if len(lists):
        l = l + lists[-1]
    else:
        return None
    return l
