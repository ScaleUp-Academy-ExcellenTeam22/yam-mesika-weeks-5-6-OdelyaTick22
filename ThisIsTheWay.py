from os import listdir


def way(path: str) -> list[str]:
    """
    A function that gets a path to a folder,
    and returns the list of all files that begin with the "deep" letter sequence in that folder
    @param path: a path to a folder
    @return list of all files that begin with the "deep" letter sequence in that folder
    """
    files = []
    arr = listdir(path)
    [files.append(name) for name in list(arr) if name.startswith("deep")]
    return files

"""
An example usage:
print(way(r"C:\Users\IMOE001\Downloads"))
>>['deep.txt', 'deepmkvgk.txt']
"""