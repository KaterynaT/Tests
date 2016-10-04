"""
We have any integer from 1 to 999 - doesn't matter, in short, this is just a function variable.
We need to represent it as string of digits like "000001" or "000999" correspondingly.
The number of digits may vary.
"""

def digstr(number, zeronum = 6 ):
    """
    :param number: any integer from 1 to 999
    :param zeronum: the number of digits
    :return: a string of digits like "000001" or "000999"
    """
    a = str(number).zfill(zeronum)
    return a

if __name__ == "__main__":
    print(digstr(345))

