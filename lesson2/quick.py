import random


def quick_sort(list):
    if len(list) <= 1:
        return list
    else:
        random_element = random.choice(list)
        less_random = []
        equal_ramdom = []
        greater_random  = []
        for elem in list:
            if elem < random_element:
                less_random.append(elem)
            elif elem > random_element:
                greater_random.append(elem)
            else:
                equal_ramdom.append(elem)
        return quick_sort(less_random) + equal_ramdom + quick_sort(greater_random)

print quick_sort([54,26,93,17,77,31,44,55,20])