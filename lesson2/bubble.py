def bubble_sort(list):
    for numbers in range(len(list)-1,0,-1):
        for i in range(numbers):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp

list = [54,26,93,17,77,31,44,55,20]
bubble_sort(list)
print(list)