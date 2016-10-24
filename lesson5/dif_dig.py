from collections import Counter
def unique_lists(first_list, second_list):
    counter1 = Counter(first_list)
    counter2 = Counter(second_list)
    common= list(counter1&counter2)
    for i in common:
        del counter1[i]
        del counter2[i]
    print (list(counter1.elements()))
    print (list(counter2.elements()))
    return (list(counter1.elements()),list(counter2.elements()))


if __name__ == "__main__":
    unique_lists([2, 2, 2, 3, 7, 78, 90], [5, 5, 5, 3])