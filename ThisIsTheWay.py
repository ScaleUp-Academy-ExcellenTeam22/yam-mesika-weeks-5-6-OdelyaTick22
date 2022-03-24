from os import listdir


def way(path):
    files = []
    arr = listdir(path)
    for name in arr:
        if name.startswith("deep"):
            files.append(name)
    return files

