"""We have the string like "AAA BBB CCC DDD EEE FFF GGG"""""
"""The task is to split the string by any symbol and to sort the contents in the reversed order"""

def revline(line, x=','):

    a = line.split(x)
    a.sort(reverse=True)
    return a

if __name__ == "__main__":
    print(revline("AAA BBB CCC DDD EEE FFF GGG"))
