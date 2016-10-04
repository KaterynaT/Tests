"""
We have any integer from 1 to 999 - doesn't matter, in short, this is just a function variable.
We need to represent it as string of digits like "000001" or "000999" correspondingly.
"""

def digstr(number):
    """
    :param number: any integer from 1 to 999
    :return: a string of digits like "000001" or "000999"
    """
    a = ("%06d") % number
    return a

if __name__ == "__main__":
   print(digstr(567))
