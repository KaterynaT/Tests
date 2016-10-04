"""
We have the string like "AAA BBB CCC DDD EEE FFF GGG"
The task is to split the string by any symbol and to sort the contents in the reversed order
"""

def revline(line, separator=' '):
    """
    :param line: any string
    :param separator: any symbol, by which we split the string
    :return: a list with the reversed contents
    """
    a = line.split(separator)
    a.sort(reverse=True)
    return a

if __name__ == "__main__":
    print(revline("AAA BBB CCC DDD EEE FFF GGG"))
